from typing import List


class Solution:
    def increasingTriplet_tle(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        left = [nums[0]]
        right = [nums[n - 1]]
        for i in range(1, n):
            left.append(min(left[-1], nums[i]))
        for i in range(n - 2, -1, -1):
            right.insert(0, max(right[0], nums[i]))
        for i in range(n):
            if left[i] < nums[i] < right[i]:
                return True
        return False
