class Solution:
    def validPalindrome_tle(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        n = len(s)
        i = 0
        while i < n:
            new = s[:i] + s[i + 1:]
            if new == new[::-1]:
                return True
            i += 1
        return False
