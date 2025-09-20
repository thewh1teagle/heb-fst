"""
Hebrew phonemization lexicon for FST-based approach.
Contains mappings for Hebrew letters, nikud, and special cases.
"""

# Stress and special markers
STRESS_PHONEME = "ˈ"  # Primary stress marker

# Special diacritics (non-standard)
VOCAL_SHVA_DIACRITIC = "\u05bd"  # Meteg - indicates vocal shva
HATAMA_DIACRITIC = "\u05ab"  # Ole - stress marker
NIKUD_HASER_DIACRITIC = "\u05af"  # Masora - indicates no vowel
EN_GERESH = "'"  # Geresh for foreign sounds

# Hebrew consonant mappings
LETTERS_PHONEMES = {
    "א": "ʔ",  # Alef
    "ב": "v",  # Bet
    "ג": "g",  # Gimel
    "ד": "d",  # Dalet
    "ה": "h",  # He
    "ו": "v",  # Vav (consonantal)
    "ז": "z",  # Zayin
    "ח": "x",  # Het
    "ט": "t",  # Tet
    "י": "j",  # Yod
    "ך": "x",  # Kaf sofit
    "כ": "x",  # Kaf
    "ל": "l",  # Lamed
    "ם": "m",  # Mem sofit
    "מ": "m",  # Mem
    "ן": "n",  # Nun sofit
    "נ": "n",  # Nun
    "ס": "s",  # Samekh
    "ע": "ʔ",  # Ayin
    "פ": "f",  # Pe
    "ף": "f",  # Pe sofit
    "ץ": "ts", # Tsadi sofit
    "צ": "ts", # Tsadi
    "ק": "k",  # Qof
    "ר": "r",  # Resh
    "ש": "ʃ",  # Shin
    "ת": "t",  # Tav
}

# Dagesh (doubling) variants for beged kefet letters
DAGESH_PHONEMES = {
    "בּ": "b",  # Bet with dagesh
    "כּ": "k",  # Kaf with dagesh  
    "ךּ": "k",  # Kaf sofit with dagesh
    "פּ": "p",  # Pe with dagesh
    "ףּ": "p",  # Pe sofit with dagesh
}

# Shin/Sin distinction
SHIN_SIN_PHONEMES = {
    "שׁ": "ʃ",  # Shin with shin dot
    "שׂ": "s",  # Sin with sin dot
}

# Geresh for foreign sounds
GERESH_PHONEMES = {
    "ג": "dʒ", # Gimel with geresh -> j sound
    "ז": "ʒ",  # Zayin with geresh -> zh sound
    "צ": "tʃ", # Tsadi with geresh -> ch sound
    "ץ": "tʃ", # Tsadi sofit with geresh -> ch sound
    "ת": "ta", # Tav with geresh -> special case
}

# Nikud (vowel) mappings
NIKUD_PHONEMES = {
    "\u05b4": "i",  # Hiriq (i)
    "\u05b1": "e",  # Hataf segol (reduced e)
    "\u05b5": "e",  # Tsere (e)
    "\u05b6": "e",  # Segol (e)
    "\u05b2": "a",  # Hataf patah (reduced a)
    "\u05b7": "a",  # Patah (a)
    "\u05c7": "o",  # Qamats qatan (o)
    "\u05b9": "o",  # Holam (o)
    "\u05ba": "o",  # Holam haser for vav
    "\u05bb": "u",  # Qubuts (u)
    "\u05b3": "o",  # Hataf qamats (reduced o)
    "\u05b8": "a",  # Qamats (a)
    "\u05b0": "",   # Shva (silent or vocal depending on context)
    "\u05c2": "",   # Sin dot (handled by post-processing rules)
    "\u05c1": "",   # Shin dot (indicates shin should be 'ʃ', but ש already maps to ʃ)
    "\u05bc": "",   # Dagesh (handled in DAGESH_PHONEMES)
    HATAMA_DIACRITIC: STRESS_PHONEME,  # Stress marker
    VOCAL_SHVA_DIACRITIC: "e",  # Vocal shva (meteg)
}

# Unicode normalization mappings
DEDUPLICATE = {
    "\u05f3": "'",  # Hebrew geresh to ASCII apostrophe
    "־": "-",       # Hebrew maqaf to ASCII hyphen
}

# Common Unicode values for reference
SHVA = "\u05b0"
DAGESH = "\u05bc"
SIN_DOT = "\u05c2"
SHIN_DOT = "\u05c1"
PATAH = "\u05b7"
QAMATS = "\u05b8"
HOLAM = "\u05b9"
HIRIQ = "\u05b4"
QUBUTS = "\u05bb"
TSERE = "\u05b5"
SEGOL = "\u05b6"

# Special combinations that need context-sensitive handling
VAV_HOLAM_COMBINATIONS = {
    "ו" + HOLAM: "o",  # Vav with holam = o sound
    "וֹ": "o",  # Pre-composed vav holam
}

# Context-sensitive rules for vav
VAV_VOWEL_CONTEXTS = {
    HOLAM: "o",  # Vav + holam = o
    QUBUTS: "u",  # Vav + qubuts = u  
    HIRIQ: "i",  # Vav + hiriq = i (rare)
}

# Character sets for pattern matching
HEBREW_LETTERS = set(LETTERS_PHONEMES.keys())
VOWEL_NIKUD = set(NIKUD_PHONEMES.keys()) - {SHVA, HATAMA_DIACRITIC, VOCAL_SHVA_DIACRITIC}
ALL_PHONEMES = set(LETTERS_PHONEMES.values()) | set(NIKUD_PHONEMES.values()) | set(GERESH_PHONEMES.values()) | set(DAGESH_PHONEMES.values()) | set(SHIN_SIN_PHONEMES.values())
