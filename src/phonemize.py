"""
Hebrew phonemizer using Finite State Transducers (FST).
Converts Hebrew text with nikud to IPA phonemic transcription.
All phonological rules are built into the FST for standalone use.
"""

import pynini
import unicodedata
from . import fst

class HebrewPhonemizer:
    
    def __init__(self, fst_path: str):
        self.fst = fst.get_hebrew_phonemizer_fst(fst_path)

    def phonemize(self, word: str) -> str:
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
    
        
        # Apply FST to the input word - FST handles everything internally
        try:
            result = pynini.compose(normalized_word, self.fst).string()
            return result
        except pynini.FstOpError:
            return ""  # No valid path found