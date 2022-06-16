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


    def maxArea(self, height: List[int]) -> int:
        result = 0
        i = 0
        j = len(height) - 1
        while i < j:
            result = max(result, min(height[i], height[j])*(j-i))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return result
