from typing import List


class Solution:
    def isGood(self, nums) -> bool:
        nums.sort()
        if nums[0] != 1:
            return False

        n = len(nums)
        if n == 1:
            return False
        for i in range(n - 2):
            if nums[i] + 1 != nums[i + 1]:
                return False
        return True if nums[n - 2] == nums[n - 1] else False
