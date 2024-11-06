from custom_spellcheck import CustomSpellChecker

# Create test file
spell_check = CustomSpellChecker('words.txt')

# Test the same input as the original
test_string = "gld narow"
spell_check.check(test_string)

# Get suggestions and corrections
print("Suggestions:", spell_check.suggestions())
print("Correction:", spell_check.correct())

