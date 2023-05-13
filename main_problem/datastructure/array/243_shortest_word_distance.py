from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        words_position = {}
        for i, word in enumerate(wordsDict):
            words_position.setdefault(word, []).append(i)
        result = len(wordsDict)
        for i in words_position[word1]:
            for j in words_position[word2]:
                result = min(result, abs(i - j))
        return result
