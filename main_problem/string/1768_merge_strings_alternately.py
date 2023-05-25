class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        i = 0
        result = ""
        while i < n1 or i < n2:
            result += word1[i] if i < n1 else ""
            result += word2[i] if i < n2 else ""
            i += 1
        return result
