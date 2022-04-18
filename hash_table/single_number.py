from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for num in nums_set:
            nums.remove(num)
        return (nums_set - set(nums)).pop()
