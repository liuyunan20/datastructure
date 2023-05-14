from typing import List


class Solution:
    def wordBreak_tle(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        def helper(i, j):
            if i == n:
                return True
            while j < n:
                print(s[i: j + 1])
                if s[i: j + 1] and s[i: j + 1] in wordDict and helper(j + 1, j + 1):
                    return True
                else:
                    j += 1
            return False
        return helper(0, 0)
