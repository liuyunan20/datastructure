import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = {}
        for point in points:
            dist = math.sqrt(point[0] ** 2 + point[1] ** 2)
            distance.setdefault(dist, []).append(point)
        distance = sorted(distance.items())
        result = []
        while len(result) < k:
            x = distance.pop(0)
            result += x[1]
        return result
