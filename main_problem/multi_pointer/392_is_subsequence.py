class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i = 0
        j = 0
        ns = len(s)
        nt = len(t)
        while j < nt:
            if s[i] == t[j]:
                i += 1
            j += 1
            if i == ns:
                return True
        return False
