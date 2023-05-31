from typing import List


class Solution:
    def increasingTriplet_tle(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] < nums[k]:
                        return True
        return False
