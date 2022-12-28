from typing import List


class Solution:
    def maxSubArrayLen_tle(self, nums: List[int], k: int) -> int:
        n = len(nums)
        length = 0
        i = 0
        while i < n:
            sub_sum = 0
            j = i
            while j < n:
                sub_sum += nums[j]
                if sub_sum == k:
                    length = max(length, j - i + 1)
                j += 1
            i += 1
        return length
