from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        i = 0
        left = nums[0]
        middle = 2147483648
        while i < n:
            if nums[i] > middle:
                return True
            if left < nums[i]:
                middle = min(middle, nums[i])
            else:
                left = nums[i]
            i += 1
        return False
