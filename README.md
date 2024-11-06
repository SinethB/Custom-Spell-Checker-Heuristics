# Custom Spell Checker Heuristics

This project implements and compares two spell-checking algorithms in Python, applying fuzzy string matching principles to evaluate performance and accuracy.

## Project Overview

This repository includes:
- **Original FuzzyWuzzy-Based Spell Checker:** Uses the FuzzyWuzzy library, which leverages the Levenshtein Distance to provide a similarity index (score) between 0 and 100.
- **Custom Heuristic Spell Checker:** Designed with a unique scoring system to evaluate and suggest word corrections more accurately. This heuristic considers factors like sequence similarity, first-letter match, length similarity, and shared characters to achieve better accuracy and relevance in word suggestions.

The project satisfies the following tasks:
1. **Apply Artificial Intelligence Techniques:** By developing and comparing two spell-checking algorithms.
2. **Design and Implement Custom Heuristics:** A custom spell checker was created based on a multi-component scoring system.
3. **Evaluate Performance Metrics:** Compared metrics (accuracy, precision, recall, speed) to identify the strengths and weaknesses of each algorithm.

## Task Instructions (ILO)
- **Objective:** To apply AI models and principles to solve spell-checking problems.
- **Application 01:** Implement and understand the FuzzyWuzzy library for string similarity matching.
- **Application 02:** Design a custom heuristic and compare it to the FuzzyWuzzy-based spell checker.

## Features
1. **Original Spell Checker (FuzzyWuzzy):**
   - Uses the FuzzyWuzzy library.
   - Calculates string similarity using Levenshtein Distance.
   - Suggests corrections based on a similarity threshold (75%).

2. **Custom Heuristic Spell Checker:**
   - Considers multiple factors (sequence similarity, first-letter match, length, and common characters).
   - Provides highly accurate suggestions with 100% precision and recall.
   - Suitable for applications prioritizing accuracy over processing speed.

## Performance Metrics
- **Accuracy**: Percentage of words correctly corrected.
- **Precision**: Relevance of the suggestions.
- **Recall**: Coverage of correct words in suggestions.
- **Speed**: Words processed per second.

## Screenshots and Output
Output screenshots and metrics comparisons can be found in the `output.pdf` file.

## How to Run
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/Custom-Spell-Checker-Heuristics.git
    cd Custom-Spell-Checker-Heuristics
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:
    for Original FuzzyWuzzy-Based Spell Checker
    ```bash
    python spellcheck_demo.py
    ```
    for custom made heuristic spell checker
   ```bash
    python custom_spellcheck_demo.py
    ```

## References
- **FuzzyWuzzy Library:** Uses Levenshtein Distance for fuzzy string matching.
- **Custom Heuristics:** Based on a combined scoring approach for improved accuracy.

## License
This project is licensed under the MIT License.
