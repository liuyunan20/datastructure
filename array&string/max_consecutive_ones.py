from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        start = -1
        end = 0
        for i, num in enumerate(nums):
            if num == 0:
                start = i
            if num == 1:
                end = i
            if result < end - start:
                result = end - start
        return result
