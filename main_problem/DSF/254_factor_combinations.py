from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n < 2:
            return []
        result = []

        def dfs(comb, idx, prod):
            if comb:
                comb.append(prod)
                result.append(list(comb))
                comb.pop()
                return
            for i in range(idx, int(math.sqrt(prod) + 1)):
                if prod % i == 0:
                    comb.append(i)
                    dfs(comb, i, prod // i)
                    comb.pop()

        dfs([], 2, n)
        return result
