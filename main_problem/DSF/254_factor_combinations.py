from typing import List


class Solution:
    def getFactors_tle(self, n: int) -> List[List[int]]:
        if n < 2:
            return []
        result = []

        def dfs(comb, idx, prod):
            if prod == 1:
                result.append(list(comb))
                return
            if prod < 1:
                return
            for i in range(idx, n // 2 + 1):
                comb.append(i)
                dfs(comb, i, prod / i)
                comb.pop()
        dfs([], 2, n)
        return result
