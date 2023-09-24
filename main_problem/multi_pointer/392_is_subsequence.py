class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        ns, nt = len(s), len(t)
        while i < ns and j < nt:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return False if i < ns and j == nt else True
