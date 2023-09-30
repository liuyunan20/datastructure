class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        n = len(s)
        letters = {}
        result = 0
        while j < n:
            if s[j] not in letters:
                letters[s[j]] = j
                result = max(result, j - i + 1)
            else:
                i = letters[s[j]] + 1
                letters[s[j]] = j
                keys = list(letters.keys())
                for l in keys:
                    if letters[l] < i:
                        letters.pop(l)
            j += 1
        return result
