from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = []
        result = [0 for _ in range(len(nums))]
        product = 1
        for i, num in enumerate(nums):
            if num == 0:
                zeros.append(i)
            else:
                product *= num

        if len(zeros) == 1:
            result[zeros[0]] = product
        if len(zeros) == 0:
            for i in range(len(nums)):
                result[i] = product // nums[i]
        return result
