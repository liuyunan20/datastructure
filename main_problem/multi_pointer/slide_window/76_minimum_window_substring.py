class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def helper(f1, f2):
            for letter in f1:
                if f2.get(letter) is None or f1[letter] > f2[letter]:
                    return False
            return True
        t_freq = {}
        for letter in t:
            t_freq.setdefault(letter, 0)
            t_freq[letter] += 1
        i = j = 0
        n = len(s)
        s_freq = {}
        length = n + 1
        while j <= n:
            if helper(t_freq, s_freq):
                if length > j - i:
                    length = j - i
                    start = i
                    end = j
                s_freq[s[i]] -= 1
                i += 1
            elif j < n:
                s_freq.setdefault(s[j], 0)
                s_freq[s[j]] += 1
                j += 1
            else:
                break
        if length == n + 1:
            return ""
        else:
            if end == n:
                return s[start:]
            return s[start: end]
