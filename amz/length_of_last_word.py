class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        i = -1
        while i >= -len(s) and s[i] != " ":
            i -= 1
        return -i - 1
