import pytest
import pandas as pd
from pathlib import Path
from src.phonemize import HebrewPhonemizer

BASE_PATH = Path(__file__).parent
BASIC_CSV_PATH = BASE_PATH / "basic.csv"
FST_PATH = BASE_PATH / "hebrew_phonemizer.fst"

# Load CSV once
df = pd.read_csv(BASIC_CSV_PATH)
fst = HebrewPhonemizer(FST_PATH)

# Parametrize: each row becomes its own pytest test
@pytest.mark.parametrize("word,expected", df.values.tolist())
def test_phonemize(word, expected):
    got = fst.phonemize(word)
    assert got == expected, f"{word}: got {got}, expected {expected}"
