from typing import List


class Solution:
    def containsNearbyAlmostDuplicate_tle(self, nums: List[int], k: int, t: int) -> bool:
        for i, num in enumerate(nums):
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if abs(num - nums[j]) <= t:
                    return True
        return False
