from typing import List


class Solution:
    def wordBreak_tle(self, s: str, wordDict: List[str]) -> bool:
        letter_set = set(list(''.join(wordDict)))
        if not set(list(s)).issubset(letter_set):
            return False
        wordDict = set(wordDict)
        n = len(s)

        def helper(i, j):
            if i == n:
                return True
            while j < n:
                if s[i: j + 1] and s[i: j + 1] in wordDict and helper(j + 1, j + 1):
                    return True
                else:
                    j += 1
            return False

        return helper(0, 0)
