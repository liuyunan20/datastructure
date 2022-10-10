from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index = {}
        for i, num in enumerate(nums):
            if target - num in value_index:
                return [value_index[target-num], i]
            value_index[num] = i


t = Solution()
print(t.twoSum([4, 2, 7, 11, 15], 9))
