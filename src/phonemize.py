"""
Hebrew phonemizer using Finite State Transducers (FST).
Converts Hebrew text with nikud to IPA phonemic transcription.
All phonological rules are built into the FST for standalone use.
"""

import pynini
import unicodedata
from . import lexicon
import os


# Global FST cache
_HEBREW_FST = None
_FST_FILE_PATH = "hebrew_phonemizer.fst"


def phonemize(word: str) -> str:
    """
    Convert Hebrew word with nikud to phonemic transcription.
    
    Args:
        word: Hebrew word with nikud (vowel marks)
        
    Returns:
        IPA phonemic transcription with stress marks
    """
    if not word.strip():
        return ""
    
    # Normalize Unicode and clean input
    normalized_word = unicodedata.normalize('NFC', word.strip())
    
    # Get or create the Hebrew phonemization FST
    fst = get_hebrew_phonemizer_fst()
    
    # Apply FST to the input word - FST handles everything internally
    try:
        result = pynini.compose(normalized_word, fst).string()
        return result
    except pynini.FstOpError:
        return ""  # No valid path found


def get_hebrew_phonemizer_fst():
    """Get the Hebrew phonemizer FST, loading from file or creating new."""
    global _HEBREW_FST
    
    if _HEBREW_FST is None:
        if os.path.exists(_FST_FILE_PATH):
            # Load from file
            _HEBREW_FST = pynini.Fst.read(_FST_FILE_PATH)
        else:
            # Create new FST and save it
            _HEBREW_FST = create_hebrew_phonemizer_fst()
            _HEBREW_FST.write(_FST_FILE_PATH)
    
    return _HEBREW_FST


def create_hebrew_phonemizer_fst():
    """Create a comprehensive Hebrew phonemization FST with all rules built-in."""
    
    # Step 1: Create basic character mappings
    basic_fst = create_basic_character_fst()
    
    # Step 2: Apply context-dependent rewrite rules
    rules_fst = apply_phonological_rules(basic_fst)
    
    # Step 3: Add default stress placement for words without explicit stress
    stress_fst = add_default_stress_rule(rules_fst)
    
    return stress_fst.optimize()


def create_basic_character_fst():
    """Create basic character-to-phoneme mappings."""
    
    mapping_pairs = []
    
    # Multi-character combinations first (higher priority)
    # Shin/Sin combinations
    for hebrew_char, phoneme in lexicon.SHIN_SIN_PHONEMES.items():
        mapping_pairs.append((hebrew_char, phoneme))
    
    # Dagesh combinations
    for hebrew_char, phoneme in lexicon.DAGESH_PHONEMES.items():
        mapping_pairs.append((hebrew_char, phoneme))
    
    # Hebrew letters - basic mappings (lower priority)
    for hebrew_char, phoneme in lexicon.LETTERS_PHONEMES.items():
        mapping_pairs.append((hebrew_char, phoneme))
    
    # Nikud (vowels)
    for nikud_char, phoneme in lexicon.NIKUD_PHONEMES.items():
        if phoneme:
            mapping_pairs.append((nikud_char, phoneme))
        else:
            mapping_pairs.append((nikud_char, ""))  # Delete empty phonemes
    
    # Special diacritics
    mapping_pairs.extend([
        (lexicon.HATAMA_DIACRITIC, lexicon.STRESS_PHONEME),
        (lexicon.VOCAL_SHVA_DIACRITIC, "e"),
        ("\u05c1", ""),  # Shin dot
        ("\u05c2", ""),  # Sin dot
        ("\u05bc", ""),  # Dagesh (will be handled by rules)
    ])
    
    # Create basic FST
    basic_fst = pynini.string_map(mapping_pairs)
    return pynini.closure(basic_fst)


def apply_phonological_rules(basic_fst):
    """Apply Hebrew phonological rules using context-dependent rewriting."""
    
    # Define alphabet for rules
    alphabet = pynini.union(
        # Hebrew letters
        *[c for c in lexicon.HEBREW_LETTERS],
        # Phonemes
        "a", "e", "i", "o", "u", "ʔ", "b", "v", "g", "d", "h", "z", "x", "t", "j", "k", "l", "m", "n", "s", "f", "p", "ts", "r", "ʃ",
        # Special markers
        lexicon.STRESS_PHONEME
    )
    
    # Start with basic FST
    result_fst = basic_fst
    
    # Rule 1: Vav + Holam = o (replace "vo" with "o")
    vav_holam_rule = pynini.cdrewrite(
        pynini.cross("vo", "o"),
        "",  # No left context constraint
        "",  # No right context constraint
        pynini.closure(alphabet)
    )
    result_fst = pynini.compose(result_fst, vav_holam_rule)
    
    # Rule 2: Vav with dagesh = u (vav + dagesh produces 'u' sound, not 'v')
    # This handles the case where vav has dagesh but no explicit vowel
    vav_dagesh_rule = pynini.cdrewrite(
        pynini.cross("v", "u"),
        "",  # No left context
        pynini.union("r", "l", "m", "n", "t", "k", "s", "ʃ", "x", "h", "d", "g", "z", "p", "f", "ts", "ʔ", "j"),  # Before consonant
        pynini.closure(alphabet)
    )
    result_fst = pynini.compose(result_fst, vav_dagesh_rule)
    
    # Rule 3: Kaf dagesh correction (only for kaf, not het)
    # This is tricky - we need to distinguish kaf+dagesh from het
    # Since both map to 'x', we'll use context: kaf+dagesh typically appears with 'k' sound in certain positions
    # For now, let's remove this rule since it's causing het to be incorrectly mapped
    # TODO: Implement more sophisticated kaf/het distinction if needed
    # kaf_dagesh_rule = pynini.cdrewrite(
    #     pynini.cross("x", "k"),
    #     "",  # Any context
    #     pynini.union("a", "e", "i", "o", "u"),  # Before vowel (indicates dagesh was present)
    #     pynini.closure(alphabet)
    # )
    # result_fst = pynini.compose(result_fst, kaf_dagesh_rule)
    
    # Rule 4: Hiriq + Yod = i (replace "ij" with "i")
    hiriq_yod_rule = pynini.cdrewrite(
        pynini.cross("ij", "i"),
        "",
        "",
        pynini.closure(alphabet)
    )
    result_fst = pynini.compose(result_fst, hiriq_yod_rule)
    
    # Rule 5: Final alef deletion (remove ʔ at end after vowel)
    vowel_set = pynini.union("a", "e", "i", "o", "u")
    final_alef_rule = pynini.cdrewrite(
        pynini.cross("ʔ", ""),
        vowel_set,  # After vowel
        "[EOS]",    # At end of string
        pynini.closure(alphabet)
    )
    result_fst = pynini.compose(result_fst, final_alef_rule)
    
    # Rule 6: Final he deletion (remove h at end after vowel)
    final_he_rule = pynini.cdrewrite(
        pynini.cross("h", ""),
        vowel_set,  # After vowel
        "[EOS]",    # At end of string
        pynini.closure(alphabet)
    )
    result_fst = pynini.compose(result_fst, final_he_rule)
    
    # Rule 6.5: ח גנובה (genuvah het) - final het with patah should be ax not xa
    genuvah_het_rule = pynini.cdrewrite(
        pynini.cross("xa", "ax"),  # Change xa to ax at end of word
        "",  # No left context
        "[EOS]",  # At end of string
        pynini.closure(alphabet)
    )
    result_fst = pynini.compose(result_fst, genuvah_het_rule)
    
    # Rule 6.4: Sin/Shin distinction - SIMPLIFIED
    # For now, skip complex sin/shin rules to avoid FST conflicts
    # This will be handled by expanding SHIN_SIN_PHONEMES in lexicon.py
    
    # Rule 6.6: Beged Kefet dagesh corrections
    # Handle all beged kefet letters with dagesh: ב כ ך פ ף
    
    # Bet dagesh: v -> b (when bet has dagesh)
    # Make this more restrictive - only at word beginning or after certain contexts
    bet_dagesh_rule = pynini.cdrewrite(
        pynini.cross("v", "b"),
        "[BOS]",  # Only at beginning of word
        pynini.union("a", "e", "i", "o", "u"),  # Before vowels
        pynini.closure(alphabet)
    )
    result_fst = pynini.compose(result_fst, bet_dagesh_rule)
    
    # Kaf/Kaf sofit dagesh: x -> k (when kaf has dagesh)
    kaf_dagesh_rule = pynini.cdrewrite(
        pynini.cross("x", "k"),
        "",  # No left context restriction
        pynini.union("o", "e", "a"),  # Before vowels that commonly follow kaf+dagesh
        pynini.closure(alphabet)
    )
    result_fst = pynini.compose(result_fst, kaf_dagesh_rule)
    
    # Pe/Pe sofit dagesh: f -> p (when pe has dagesh)
    pe_dagesh_rule = pynini.cdrewrite(
        pynini.cross("f", "p"),
        "",  # No left context restriction
        pynini.union("a", "e", "i", "o", "u"),  # Before vowels
        pynini.closure(alphabet)
    )
    result_fst = pynini.compose(result_fst, pe_dagesh_rule)
    
    # Rule 7: Stress movement (move stress before vowels) - SIMPLIFIED
    # Pattern: vowel + stress -> stress + vowel
    # Only apply to common cases to avoid FST complexity
    for vowel in ["a", "e", "i", "o", "u"]:
        stress_move_rule = pynini.cdrewrite(
            pynini.cross(vowel + lexicon.STRESS_PHONEME, lexicon.STRESS_PHONEME + vowel),
            "",
            "",
            pynini.closure(alphabet)
        )
        result_fst = pynini.compose(result_fst, stress_move_rule)
    
    return result_fst


def add_default_stress_rule(fst):
    """Add default stress placement for words without explicit stress markers."""
    
    vowels = pynini.union("a", "e", "i", "o", "u")
    consonants = pynini.union("ʔ", "b", "v", "g", "d", "h", "z", "x", "t", "j", "k", "l", "m", "n", "s", "f", "p", "ts", "r", "ʃ")
    all_phonemes = pynini.union(vowels, consonants, lexicon.STRESS_PHONEME)
    
    # Strategy: Create two separate transducers and union them
    # 1. Identity for strings that already have stress
    # 2. Add-stress transducer for strings without stress
    
    # Create identity transducer for strings with stress
    # This matches any string that contains the stress phoneme
    has_stress_identity = create_identity_with_stress(all_phonemes)
    
    # Create add-stress transducer for strings without stress
    # This adds stress before the last vowel in strings that don't have stress
    add_stress_transducer = create_add_stress_transducer(vowels, consonants)
    
    # Apply both transducers to the main FST and union the results
    fst_with_stress_preserved = pynini.compose(fst, has_stress_identity)
    fst_with_stress_added = pynini.compose(fst, add_stress_transducer)
    
    # Union both paths
    result_fst = pynini.union(fst_with_stress_preserved, fst_with_stress_added)
    
    return result_fst


def create_identity_with_stress(all_phonemes):
    """Create identity transducer that only accepts strings with stress."""
    
    # Create a transducer that matches strings containing stress and passes them through unchanged
    # Pattern: (phoneme)* STRESS (phoneme)*
    
    phoneme_list = ["a", "e", "i", "o", "u", "ʔ", "b", "v", "g", "d", "h", "z", "x", "t", "j", "k", "l", "m", "n", "s", "f", "p", "ts", "r", "ʃ"]
    
    # Create identity mappings for each phoneme
    identity_mappings = [pynini.cross(p, p) for p in phoneme_list]
    prefix = pynini.closure(pynini.union(*identity_mappings))
    
    stress_part = pynini.cross(lexicon.STRESS_PHONEME, lexicon.STRESS_PHONEME)
    
    # Suffix can include stress too
    suffix_phonemes = phoneme_list + [lexicon.STRESS_PHONEME]
    suffix_mappings = [pynini.cross(p, p) for p in suffix_phonemes]
    suffix = pynini.closure(pynini.union(*suffix_mappings))
    
    return pynini.concat(prefix, pynini.concat(stress_part, suffix))


def create_add_stress_transducer(vowels, consonants):
    """Create transducer that adds stress before last vowel in strings without stress."""
    
    # Create the rule using cdrewrite with full alphabet
    add_stress_rule = pynini.cdrewrite(
        pynini.cross("", lexicon.STRESS_PHONEME),
        pynini.closure(pynini.union(vowels, consonants)),  # Any prefix
        pynini.concat(vowels, pynini.concat(pynini.closure(consonants), "[EOS]")),  # vowel + consonants + end
        pynini.closure(pynini.union(vowels, consonants, lexicon.STRESS_PHONEME))  # Full alphabet
    )
    
    # Restrict input to strings without stress (only vowels and consonants)
    no_stress_input = pynini.closure(pynini.union(vowels, consonants))
    
    # Compose: only apply to inputs without stress
    return pynini.compose(no_stress_input, add_stress_rule)