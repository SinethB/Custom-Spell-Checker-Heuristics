import time
from spellcheck import SpellCheck
from custom_spellcheck import CustomSpellChecker

def calculate_metrics(checker, test_cases, iterations=100):
    """Calculate metrics with speed in words per second"""
    total_time = 0
    total_words = len(test_cases) * iterations  # Total words processed
    
    # Run multiple iterations for more accurate timing
    for _ in range(iterations):
        start_time = time.perf_counter()
        
        total_cases = len(test_cases)
        correct_fixes = 0
        total_suggestions = 0
        correct_suggestions = 0
        still_invalid = 0
        true_positives = 0
        
        valid_words = set(['wide', 'narrow', 'area', 'light', 'glad'])
        
        for wrong_word, correct_word in test_cases:
            checker.check(wrong_word)
            correction = checker.correct().strip()
            suggestions = checker.suggestions()
            
            if correction == correct_word:
                correct_fixes += 1
                
            if correction not in valid_words:
                still_invalid += 1
                
            total_suggestions += len(suggestions)
            correct_suggestions += sum(1 for s in suggestions if s == correct_word)
            
            if correct_word in suggestions:
                true_positives += 1
        
        total_time += time.perf_counter() - start_time
    
    # Calculate words per second
    words_per_second = total_words / total_time if total_time > 0 else 0
    
    metrics = {
        'invalid_after_checker': (still_invalid / total_cases) * 100,
        'accuracy': (correct_fixes / total_cases) * 100,
        'precision': (correct_suggestions / total_suggestions * 100) if total_suggestions > 0 else 0,
        'speed': words_per_second,  
        'recall': (true_positives / total_cases) * 100
    }
    
    return metrics

# Test cases
test_cases = [
    ("gld", "glad"),
    ("narow", "narrow"),
    ("wde", "wide"),
    ("ligt", "light"),
    ("rea", "area"),
    ("glaaaad", "glad"),
    ("narrowww", "narrow"),
    ("widde", "wide"),
    ("lightt", "light"),
    ("arae", "area"),
]

# Test both spell checkers
original_checker = SpellCheck('words.txt')
custom_checker = CustomSpellChecker('words.txt')

original_metrics = calculate_metrics(original_checker, test_cases)
custom_metrics = calculate_metrics(custom_checker, test_cases)

# Print results
print("\nComparison Results:\n")
print(f"{'Metric':<25} {'Original':>10} {'Custom':>10}")
print("-" * 45)
for metric in original_metrics:
    original_value = original_metrics[metric]
    custom_value = custom_metrics[metric]
    if metric == 'speed':
        original_value = f"{original_value:.2f}w/s"
        custom_value = f"{custom_value:.2f}w/s"
    else:
        original_value = f"{original_value:.2f}%"
        custom_value = f"{custom_value:.2f}%"
    print(f"{metric.replace('_', ' ').title():<25} {original_value:>10} {custom_value:>10}")