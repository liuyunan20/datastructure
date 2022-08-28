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

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(comb, tgt, idx):
            if tgt == 0:
                result.append(list(comb))
                return
            if tgt < 0:
                return
            for i in range(idx, len(candidates)):
                # i > idx skip same candidate in this level loop;
                # if i > 0, skip all duplicate candidates
                # that's means use one number only once
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                comb.append(candidates[i])
                dfs(comb, tgt - candidates[i], i + 1)
                comb.pop()

        dfs([], target, 0)
        return result
