from typing import List


class Solution:
    def longestOnes_tle(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        j = 1
        result = 0
        while j <= n:
            if j - i - sum(nums[i: j]) <= k:
                j += 1
            else:
                i += 1
            result = max(result, j - i - 1)
        return result
