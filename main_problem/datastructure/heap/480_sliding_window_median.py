import heapq
from typing import List


class Solution:
    def medianSlidingWindow_tle(self, nums: List[int], k: int) -> List[float]:
        result = []
        for i in range(len(nums) - k):
            window = nums[i: i + k]
            if k % 2 == 1:
                n = k // 2 + 1
                result.append(heapq.nsmallest(n, window)[-1])
            if k % 2 == 0:
                n = k // 2
                l = heapq.nsmallest(n + 1, window)
                result.append((l[-1] + l[-2]) / 2)
        return result
