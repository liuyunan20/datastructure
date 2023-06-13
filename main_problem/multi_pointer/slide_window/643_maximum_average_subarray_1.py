from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if k == 1:
            return max(nums)
        i = 0
        result = sum(nums[: k]) / k
        sum_b = result
        while i < n - k:
            sum_b += (nums[i + k] - nums[i]) / k
            result = max(result, sum_b)
            i += 1
        return result
