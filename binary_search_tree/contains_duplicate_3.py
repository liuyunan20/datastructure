from typing import List
from sortedcontainers import SortedList


class Solution:
    def containsNearbyAlmostDuplicate_tle(self, nums: List[int], k: int, t: int) -> bool:
        for i, num in enumerate(nums):
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if abs(num - nums[j]) <= t:
                    return True
        return False

# use sorted list to contain k numbers
def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        sl = SortedList()
        for i, num in enumerate(nums):
            sl.add(num)
            if i > k:
                sl.remove(nums[i - k - 1])
            index = sl.index(num)
            if (index > 0 and abs(sl[index - 1] - num) <= t) or (index < len(sl) - 1 and abs(sl[index + 1] - num) <= t):
                return True
        return False
