from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(tgt, idx, combs):
            if tgt < 0:
                return
            if tgt == 0:
                result.append(list(combs))
                return
            for i in range(idx, len(candidates)):
                combs.append(candidates[i])
                new_target = tgt - candidates[i]
                dfs(new_target, i, combs)
                combs.pop()

        dfs(target, 0, [])
        return result
