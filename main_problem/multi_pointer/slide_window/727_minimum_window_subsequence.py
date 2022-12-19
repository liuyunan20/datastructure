class Solution:
    def minWindow_tle(self, s1: str, s2: str) -> str:
        i = 0
        n = len(s1)
        starts = []
        indexes = []
        while i < n:
            if s1[i] == s2[0]:
                starts.append(i)
            if s1[i] in s2:
                indexes.append(i)
            i += 1
        if len(s2) == 1 and starts:
            return s1[starts[0]]
        length = n + 1
        start = 0
        for i in starts:
            s2l = list(s2)
            s2l.pop(0)
            for j in indexes:
                # print(i, j)
                # print(s2l)
                if j > i and s1[j] == s2l[0]:
                    s2l.pop(0)
                # print(s2l)
                if not s2l:
                    if length > j - i + 1:
                        length = j - i + 1
                        start = i
                    break
        if length == n + 1:
            return ''
        return s1[start: start + length]
