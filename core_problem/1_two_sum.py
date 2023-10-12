from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            indices.setdefault(num, []).append(i)
        for num in indices:
            if target - num in indices:
                if target - num == num and len(indices[num]) == 2:
                    return indices[num]
                if target - num != num:
                    return [indices[num][0], indices[target - num][0]]
