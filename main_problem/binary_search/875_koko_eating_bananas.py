import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        def eat_time(k):
            i = 0
            for pile in piles:
                if pile <= k:
                    i += 1
                else:
                    i += math.ceil(pile / k)
            return i

        start = 1
        end = max(piles)
        while start < end:
            k = (start + end) // 2
            time = eat_time(k)
            if time <= h:
                end = k
            if time > h:
                start = k + 1
        return start
