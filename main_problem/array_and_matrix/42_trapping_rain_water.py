class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        n = len(height)
        water = 0
        high_idx = []
        high_level = []
        while i < n:
            if i == 0 and i + 1 < n and height[i] >= height[i + 1]:
                high_idx.append(i)
                high_level.append(height[i])
            if i - 1 >= 0 and i + 1 < n and height[i - 1] <= height[i] and height[i] >= height[i + 1]:
                high_idx.append(i)
                high_level.append(height[i])
            if i == n - 1 and i - 1 >= 0 and height[i - 1] <= height[i]:
                high_idx.append(i)
                high_level.append(height[i])
            i += 1
        if len(high_idx) < 2:
            return 0
        tops = [high_idx.pop(0)]
        left_level = high_level.pop(0)
        next_top = max(high_level)
        i = 0
        while next_top and i < len(high_level):
            if high_level[i] == next_top or high_level[i] >= left_level:
                tops.append(high_idx[i])
                left_level = high_level[i]
            next_top = max(high_level[i + 1:]) if high_level[i + 1:] else 0
            i += 1
        left = tops.pop(0)
        water = 0
        while tops:
            right = tops.pop(0)
            level = min(height[left], height[right])
            for j in range(left, right):
                water += max(level - height[j], 0)
            left = right
        return water
