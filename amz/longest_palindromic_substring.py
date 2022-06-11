class Solution:
    def longestPalindrome_tle(self, s: str) -> str:
            result = s[0]
            length = 0
            for i in range(len(s) - 1):
                for j in range(i, len(s)):
                    sub = s[i:j + 1]
                    if sub == sub[::-1] and len(sub) > length:
                            length = len(sub)
                            result = sub
            return result
