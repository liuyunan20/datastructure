class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        n = len(height)
        water = 0
        edge = []
        top1 = top2 = max(height)
        while i < n:
            edge.append([top1, 0])
            if height[i] == top1 and i + 1 < n:
                top1 = max(height[i + 1:])
            i += 1
        i = n - 1
        while i >= 0:
            edge[i][1] = top2
            if height[i] == top2 and i > 0:
                top2 = max(height[:i])
            i -= 1
        for i, top in enumerate(edge):
            water += min(top) - height[i]
        return water
