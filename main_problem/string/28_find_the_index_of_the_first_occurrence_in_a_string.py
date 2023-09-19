class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        n1 = len(needle)
        n2 = len(haystack)
        i = 0
        while i < n2 - n1 + 1:
            if needle == haystack[i: i + n1]:
                return i
            i += 1
        return -1
