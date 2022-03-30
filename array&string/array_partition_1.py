from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        sums = 0
        while i < len(nums):
            sums += nums[i]
            i += 2
        return sums
