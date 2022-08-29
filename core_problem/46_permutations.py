from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        results = []
        for i in range(len(nums)):
            permutes = self.permute(nums[:i] + nums[i+1:])
            for permute in permutes:
                permute.append(nums[i])
            results += permutes
        return results
