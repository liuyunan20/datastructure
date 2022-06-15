from typing import List


class Solution:
    def maxArea_tle(self, height: List[int]) -> int:
        result = 0
        for i, h in enumerate(height):
            water = 0
            for j in range(i):
                water = max(water, min(height[j], h)*(i-j))
            result = max(water, result)
        return result
