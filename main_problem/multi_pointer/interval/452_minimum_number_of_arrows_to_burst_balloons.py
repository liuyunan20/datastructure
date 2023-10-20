class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        result = 1
        current = points[0]
        for p in points:
            if p[0] > current[1]:
                current = p
                result += 1
            else:
                current[0] = max(current[0], p[0])
                current[1] = min(current[1], p[1])
        return result
