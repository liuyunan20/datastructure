class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        n = len(height)

        result = 0
        low = []
        while i < n:
            if i - 1 >= 0 and i + 1 < n and height[i - 1] < height[i] < height[i + 1]:
                low.append(height[i])
            i += 1
        while low:
            water = 0
            i = low.pop()
            left = i - 1
            while left - 1 >= 0 and height[left - 1] > height[left]:
                left -= 1
            right = i + 1
            while right + 1 < n and height[right + 1] > height[right]:
                right += 1
            top = max(height[left], height[right])
            for j in range(left + 1, right):
                water += height[j] - height[i]
