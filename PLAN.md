# Hebrew Phonemizer Implementation Plan

## Rules for Implementation (What NOT to do)

### 1. NO HARDCODING
- ❌ Do not hardcode specific Hebrew words or their phonetic representations
- ❌ Do not create lookup tables for individual words
- ❌ Do not hardcode Unicode values directly in the main logic
- ✅ Use systematic rules and patterns that work for any Hebrew word

### 2. NO COMPLEX DEPENDENCIES
- ❌ Do not import complex external libraries beyond pynini
- ❌ Do not rely on external phonemization services
- ❌ Do not use machine learning models
- ✅ Use rule-based FST approach with pynini

### 3. NO BRITTLE PARSING
- ❌ Do not assume specific word lengths or structures
- ❌ Do not use position-based character extraction
- ❌ Do not assume specific nikud patterns
- ✅ Create robust FST rules that handle various Hebrew text patterns

### 4. NO INCOMPLETE IMPLEMENTATIONS
- ❌ Do not return placeholder values or incomplete phonemizations
- ❌ Do not skip difficult cases
- ❌ Do not ignore stress marks or special characters
- ✅ Handle all test cases systematically

## Implementation Strategy

### Phase 1: Core FST Structure
1. Create character mapping FSTs (Hebrew letters → phonemes)
2. Create nikud (vowel) mapping FSTs
3. Handle special cases (dagesh, geresh, etc.)

### Phase 2: Rule Implementation
1. Consonant rules (including beged kefet)
2. Vowel rules (including reduced vowels)
3. Stress placement rules
4. Special letter combinations

### Phase 3: Integration
1. Compose all FSTs into a single transducer
2. Apply to input Hebrew text
3. Extract phonemic output

### Phase 4: Testing & Refinement
1. Run against test cases
2. Debug systematic issues
3. Refine rules without hardcoding

## Key Technical Decisions

- Use pynini for FST construction and composition
- Implement systematic rules based on Hebrew phonology
- Handle Unicode normalization properly
- Maintain the simple interface: `phonemize(word: str) -> str`
- Return IPA phonemic transcription with stress marks

## Success Criteria

- All 279 test cases pass
- No hardcoded word-specific mappings
- Robust handling of various Hebrew text patterns
- Clean, maintainable FST-based implementation

## Testing Optimization

### Current Status: 15/20 (75%) test cases passing

### Testing Strategy for Efficiency
- **Skip working cases**: Once cases are verified working, add `--skip N` argument to skip first N cases
- **Focus on new cases**: Test cases beyond the known working ones to avoid regression testing
- **Batch testing**: Test ranges of cases (e.g., cases 21-40) instead of full suite
- **Progressive validation**: Start with first 20, then 50, then 100, finally all 279

### Implementation Ideas
```python
# In test_phonemize.py
def test_phonemize(skip=0, limit=None):
    # Skip first N cases that are already working
    start_idx = skip
    end_idx = skip + limit if limit else len(df)
    test_subset = range(start_idx, min(end_idx, len(df)))
```

This allows focused testing:
- `pytest --skip 15` (skip first 15 working cases)
- `pytest --skip 15 --limit 10` (test cases 16-25 only)
- `pytest` (test all cases)
