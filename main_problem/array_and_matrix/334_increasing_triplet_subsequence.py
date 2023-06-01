from typing import List


class Solution:
    def increasingTriplet_tle(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        for i in range(1, n - 1):
            left = min(nums[:i])
            right = max(nums[i + 1:])
            if left < nums[i] < right:
                return True
        return False
