from functools import cache
from typing import List


class Solution:
    # TLE, maybe because of recursion
    def findTargetSumWays_tle(self, nums: List[int], target: int) -> int:
        def dfs(nums, target, index):
            if index == len(nums):
                return 0
            if index == len(nums) - 1:
                if nums[index] == abs(target):
                    if nums[index] == 0:
                        return 2
                    return 1
                return 0
            num = nums[index]
            a = dfs(nums, target + num, index + 1)
            b = dfs(nums, target - num, index + 1)
            return a + b
        return dfs(nums, target, 0)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(target, index):
            if index == len(nums):
                return 0
            if index == len(nums) - 1:
                if nums[index] == abs(target):
                    if nums[index] == 0:
                        return 2
                    return 1
                return 0
            num = nums[index]
            a = dfs(target + num, index + 1)
            b = dfs(target - num, index + 1)
            return a + b
        return dfs(target, 0)
