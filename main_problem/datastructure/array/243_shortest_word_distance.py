from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        words_position = {word1: -1, word2: -1}
        result = len(wordsDict)
        for i, word in enumerate(wordsDict):
            if word in words_position:
                words_position[word] = i
                if words_position[word1] >= 0 and words_position[word2] >= 0:
                    result = min(result, abs(words_position[word1] - words_position[word2]))
        return result
