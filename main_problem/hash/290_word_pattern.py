class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = s.split()
        m = len(pattern)
        n = len(s)
        if m != n:
            return False
        pattern_s = {}
        s_pattern = {}
        for i in range(n):
            if not pattern_s.get(pattern[i]) and not s_pattern.get(s[i]):
                pattern_s[pattern[i]] = s[i]
                s_pattern[s[i]] = pattern[i]
            elif pattern_s.get(pattern[i]) and s_pattern.get(s[i]) and pattern_s[pattern[i]] == s[i] and \
                    s_pattern[s[i]] == pattern[i]:
                continue
            else:
                return False
        return True
