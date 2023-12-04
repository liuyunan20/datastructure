class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        i = 1
        while i < n:
            j = 2
            while s[:i] == s[(j - 1) * i: j * i]:
                if j * i == n:
                    return True
                else:
                    j += 1
            i += 1
        return False
