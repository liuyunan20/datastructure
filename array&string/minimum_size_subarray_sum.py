from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        length = float('inf')
        result = float('inf')
        sum_sub = 0
        for i, num in enumerate(nums):
            sum_sub += num
            while sum_sub >= target:
                length = i - start + 1
                sum_sub -= nums[start]
                start += 1
            if result > length:
                result = length
        if result == float('inf'):
            return 0
        return result
