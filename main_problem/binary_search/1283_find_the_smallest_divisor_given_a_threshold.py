import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def sum_of_divisions(divisor):
            s = 0
            for num in nums:
                s += math.ceil(num / divisor)
            return s

        start = 1
        end = max(nums)
        while start < end:
            divisor = (start + end) // 2
            cur = sum_of_divisions(divisor)
            if cur <= threshold:
                end = divisor
            else:
                start = divisor + 1
        return start
