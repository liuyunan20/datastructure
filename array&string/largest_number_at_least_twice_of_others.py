from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        for i, num in enumerate(nums):
            if max_num == num:
                index = i
            elif max_num < num * 2:
                return -1
        return index
