from typing import List


class Solution:
    # brute force solution, traversal the array and find the index
    def search(self, nums: List[int], target: int) -> int:
        for i, e in enumerate(nums):
            if e == target:
                return i
        return -1
