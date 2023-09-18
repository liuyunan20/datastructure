class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        strs.sort(key=len)
        i = 0
        m = len(strs[0])
        while i < m:
            p = strs[0][i]
            for word in strs:
                if word[i] != p:
                    return prefix
            prefix += p
            i += 1
        return prefix
