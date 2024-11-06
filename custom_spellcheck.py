from difflib import SequenceMatcher
import re

class CustomSpellChecker:
    def __init__(self, word_dict_file=None):
        # Read dictionary file
        self.file = open(word_dict_file, 'r')
        data = self.file.read()
        data = data.split(",")
        data = [i.strip().lower() for i in data]
        self.dictionary = list(set(data))
        self.string_to_check = None
        
    def check(self, string_to_check):
        self.string_to_check = string_to_check.lower()
    
    def calculate_similarity_score(self, word1, word2):
        """
        Custom heuristic that combines multiple similarity metrics:
        1. Sequence similarity (using SequenceMatcher)
        2. First letter matching
        3. Length similarity
        4. Common characters
        """
        # Base sequence similarity
        sequence_similarity = SequenceMatcher(None, word1, word2).ratio() * 50
        
        # First letter bonus
        first_letter_bonus = 20 if word1[0] == word2[0] else 0
        
        # Length similarity
        len_diff = abs(len(word1) - len(word2))
        length_score = max(0, 15 - (len_diff * 3))
        
        # Common characters
        common_chars = len(set(word1) & set(word2))
        char_score = (common_chars / max(len(word1), len(word2))) * 15
        
        total_score = sequence_similarity + first_letter_bonus + length_score + char_score
        return total_score

    def suggestions(self, threshold=65):
        suggestions_list = []
        words = self.string_to_check.split()
        
        for word in words:
            word_suggestions = []
            for dict_word in self.dictionary:
                similarity = self.calculate_similarity_score(word, dict_word)
                if similarity >= threshold:
                    word_suggestions.append((dict_word, similarity))
            
            # Sort by similarity score and add to suggestions
            word_suggestions.sort(key=lambda x: x[1], reverse=True)
            suggestions_list.extend([sugg[0] for sugg in word_suggestions])
        
        return suggestions_list

    def correct(self, threshold=65):
        corrected_words = []
        words = self.string_to_check.split()
        
        for word in words:
            best_match = word
            best_score = 0
            
            for dict_word in self.dictionary:
                similarity = self.calculate_similarity_score(word, dict_word)
                if similarity >= threshold and similarity > best_score:
                    best_match = dict_word
                    best_score = similarity
            
            corrected_words.append(best_match)
        
        return " ".join(corrected_words)