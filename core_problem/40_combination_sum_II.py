from typing import List


class Solution:
    def combinationSum2_tle(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def dfs(comb, target, idx):
            if target == 0 and comb not in result:
                result.append(list(comb))
                return
            if target < 0:
                return
            for i in range(idx, len(candidates)):
                comb.append(candidates[i])
                dfs(comb, target - candidates[i], i + 1)
                comb.pop()

        dfs([], target, 0)
        return result
