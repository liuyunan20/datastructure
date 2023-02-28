from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i_tg_result = {}

        def dfs(i, tg):
            if i == n:
                if tg == 0:
                    return 1
                return 0
            if (i, tg) in i_tg_result:
                return i_tg_result[(i, tg)]
            a = dfs(i + 1, tg + nums[i])
            b = dfs(i + 1, tg - nums[i])
            i_tg_result[(i, tg)] = a + b
            return i_tg_result[(i, tg)]
        dfs(0, target)
        return i_tg_result[(0, target)]
