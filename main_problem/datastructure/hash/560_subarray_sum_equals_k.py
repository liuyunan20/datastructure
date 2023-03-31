from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if sum(nums[i: j]) == k:
                    result += 1
        return result
