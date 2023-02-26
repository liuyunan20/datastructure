from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        result = []

        def dfs(string, idx):
            if idx == n:
                result.append(" ".join(list(string)))
                print(len(string[0]))
                return len(string[0])
            for i in range(idx, n):
                cur = s[idx:i + 1]
                if cur and cur in wordDict:
                    string.append(cur)
                    dfs(string, i + 1)
                    string.pop()

        dfs([], 0)
        return result
