import math
from typing import List


class Solution:
    # brute force solution, traversal the array and find the index
    def search(self, nums: List[int], target: int) -> int:
        for i, e in enumerate(nums):
            if e == target:
                return i
        return -1

    def binary_search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            i = math.floor((right+left)/2)
            if nums[i] == target:
                return i
            elif target > nums[i]:
                left = i + 1
            else:
                right = i - 1
        return -1
