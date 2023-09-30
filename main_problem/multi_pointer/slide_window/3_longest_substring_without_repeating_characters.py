class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        n = len(s)
        letters = {}
        result = 0
        while j < n:
            if s[j] not in letters:
                letters[s[j]] = j
                j += 1
                result = max(result, j - i)
            else:
                i += 1
                letters[s[j]] = j
                j += 1
        return result
