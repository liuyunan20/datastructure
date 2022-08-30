from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        if len(nums) == 1:
            return [nums]
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            permutes = self.permuteUnique(nums[:i] + nums[i+1:])
            for permute in permutes:
                permute.append(nums[i])
            result += permutes
        return result
