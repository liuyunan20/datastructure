class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = len(g) - 1
        j = len(s) - 1
        result = 0
        while i >= 0 and j >= 0:
            if s[j] >= g[i]:
                j -= 1
                i -= 1
                result += 1
            else:
                i -= 1
        return result
