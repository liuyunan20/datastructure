class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_freq = {}
        for i in range(len(s)):
            s_freq.setdefault(s[i], []).append(i)

        t_freq = {}
        for i in range(len(t)):
            t_freq.setdefault(t[i], []).append(i)

        s_value = list(s_freq.values())
        t_value = list(t_freq.values())
        return s_value == t_value
