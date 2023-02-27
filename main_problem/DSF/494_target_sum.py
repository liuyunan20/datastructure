from typing import List


class Solution:
    def findTargetSumWays_tle(self, nums: List[int], target: int) -> int:
        n = len(nums)
        result = [0]

        def dfs(i, tg):
            if i == n:
                if tg == 0:
                    result[0] += 1
                return
            dfs(i + 1, tg + nums[i])
            dfs(i + 1, tg - nums[i])
        dfs(0, target)
        return result[0]
