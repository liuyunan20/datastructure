import heapq
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        window = nums[:k - 1]
        heapq.heapify(window)
        for i in range(k - 1, len(nums)):
            heapq.heappush(window, nums[i])
            if k % 2 == 1:
                n = k // 2 + 1
                result.append(heapq.nsmallest(n, window)[-1])
            if k % 2 == 0:
                n = k // 2
                l = heapq.nsmallest(n + 1, window)
                result.append((l[-1] + l[-2]) / 2)
            window.remove(nums[i + 1 - k])
        return result
