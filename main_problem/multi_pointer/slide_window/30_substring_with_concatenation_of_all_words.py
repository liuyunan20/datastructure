from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        word_num = len(words)
        word_len = len(words[0])
        j = word_num * word_len
        words.sort()
        result = []
        for i in range(n - j + 1):
            sub = []
            start = i
            end = i + j
            while start < end:
                sub.append(s[start: start + word_len])
                start += word_len
            if sorted(sub) == words:
                result.append(i)
        return result
