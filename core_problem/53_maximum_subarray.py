from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        current = 0
        for num in nums:
            if num < 0 and result < 0:
                result = max(result, num)
                continue
            elif current < 0:
                current = num
            else:
                current += num
            result = max(result, current)
        return result


    def maxSubArray_2(self, nums: List[int]) -> int:
        result = nums[0]
        current = 0
        for num in nums:
            if current < 0:
                current = num
            else:
                current += num
            result = max(result, current)
        return result
