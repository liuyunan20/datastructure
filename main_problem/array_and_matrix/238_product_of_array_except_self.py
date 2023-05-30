from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = 0
        i0 = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
                i0 = i
            else:
                product *= nums[i]
        if zero > 1:
            result = [0] * len(nums)
        elif zero == 1:
            result = [0] * len(nums)
            result[i0] = product
        else:
            result = []
            for num in nums:
                result.append(int(product / num))
        return result
