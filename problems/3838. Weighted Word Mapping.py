from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        char_to_weight = lambda c: weights[ord(c) - ord('a')]
        word_to_weight = lambda word: 25 - (sum(map(char_to_weight, word)) % 26)
        word_to_char = lambda word: chr(word_to_weight(word) + ord('a'))
        return ''.join(map(word_to_char, words))