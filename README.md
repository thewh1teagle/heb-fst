# Hebrew FST (Finite State Transducer)

Fast rule-based FST that converts Hebrew word with enhanced diacritics to phonemes.

_Enhanced diacritics are those from the Phonikud project_ https://phonikud.github.io/

## WIP

Goal: 
- [ ] The code should convert Hebrew word with Nikud to phonemes
- [ ] Tests should pass

## Test

```bash
uv run pytest tests/
```

## Test coverage

```bash
pytest -q --disable-warnings --tb=no --maxfail=0 | tail -n 1
```

## Gotchas

on macOS:

```console
brew install openfst
export CPLUS_INCLUDE_PATH="/opt/homebrew/include:$CPLUS_INCLUDE_PATH"
export LIBRARY_PATH="/opt/homebrew/lib:$LIBRARY_PATH"
uv pip install pynini
```