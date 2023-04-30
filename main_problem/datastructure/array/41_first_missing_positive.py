from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        n = max(nums)
        if n <= 0:
            return 1
        i = 1
        while i <= n:
            if i not in nums:
                return i
            i += 1
        return n + 1
