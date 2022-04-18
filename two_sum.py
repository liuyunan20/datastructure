from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums[i + 1:]:
                return [i, nums[i + 1:].index(target - nums[i]) + i + 1]

    def twoSum_dict(self, nums: List[int], target: int) -> List[int]:
        value_index = {}
        for i, num in enumerate(nums):
            value_index.setdefault(num, []).append(i)
        for value in value_index:
            if value == target - value and len(value_index[value]) == 2:
                return value_index[value]
            elif value != target - value and value_index.get(target - value):
                return [value_index[value][0], value_index[target - value][0]]
