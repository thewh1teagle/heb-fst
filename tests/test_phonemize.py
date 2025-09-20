from src.phonemize import phonemize
import pandas as pd
from pathlib import Path

BASE_PATH = Path(__file__).parent
BASIC_CSV_PATH = BASE_PATH / "basic.csv"

def test_phonemize():
    df = pd.read_csv(BASIC_CSV_PATH)
    for _, row in df.iterrows():
        assert phonemize(row["word"]) == row["phonemes"]