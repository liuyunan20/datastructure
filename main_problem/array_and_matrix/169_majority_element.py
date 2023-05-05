from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2
        freq = {}
        for num in nums:
            freq.setdefault(num, 0)
            freq[num] += 1
            if freq[num] > n:
                return num
