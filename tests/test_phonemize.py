import pytest
import pandas as pd
from pathlib import Path
from src.phonemize import phonemize

BASE_PATH = Path(__file__).parent
BASIC_CSV_PATH = BASE_PATH / "basic.csv"

# Load CSV once
df = pd.read_csv(BASIC_CSV_PATH)

# Parametrize: each row becomes its own pytest test
@pytest.mark.parametrize("word,expected", df.values.tolist())
def test_phonemize(word, expected):
    got = phonemize(word)
    assert got == expected, f"{word}: got {got}, expected {expected}"
