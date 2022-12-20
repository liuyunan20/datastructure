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

    def minWindow_tle2(self, s1: str, s2: str) -> str:
        i = 0
        n1 = len(s1)
        n2 = len(s2)
        starts = []
        indexes = {}
        while i < n1:
            if s1[i] in s2:
                indexes.setdefault(s1[i], []).append(i)
            i += 1
        start_letter = s2[0]
        if len(s2) == 1 and indexes.get(start_letter):
            return s1[indexes[start_letter][0]]
        if not indexes.get(start_letter):
            return ""
        length = n1 + 1
        start = 0
        has_sub = False
        find_j = False
        for i in indexes[start_letter]:
            j = 1
            current = i
            while j < n2:
                if not indexes.get(s2[j]):
                    return ""
                for index in indexes[s2[j]]:
                    if index > current:
                        current = index
                        find_j = True
                        if j == n2 - 1:
                            has_sub = True
                        break
                if not find_j:
                    break
                if has_sub and length > current - i + 1:
                    length = current - i + 1
                    start = i
                find_j = False
                has_sub = False
                j += 1

        if length == n1 + 1:
            return ''
        return s1[start: start + length]
