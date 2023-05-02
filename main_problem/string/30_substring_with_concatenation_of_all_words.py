from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words[0])
        l = n * len(words)
        m = len(s) - l
        i = 0
        res = []
        while i <= m:
            if s[i: i + n] in words:
                copy = [word for word in words]
                copy.remove(s[i: i + n])
                is_result = True
                for j in range(i + n, i + l, n):
                    if s[j: j + n] not in copy:
                        is_result = False
                        break
                    else:
                        copy.remove(s[j: j + n])
                if is_result:
                    res.append(i)
            i += 1
        return res
