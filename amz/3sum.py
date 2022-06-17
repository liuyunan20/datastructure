from typing import List


class Solution:
    def threeSum_tle(self, nums: List[int]) -> List[List[int]]:
        num_pst = {}
        result = []
        for i, num in enumerate(nums):
            num_pst.setdefault(num, []).append(i)
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                s = nums[i] + nums[j]
                if num_pst.get(-s) is not None:
                    for k in num_pst[-s]:
                        if k != i and k != j and sorted([nums[i], nums[j], nums[k]]) not in result:
                            result.append(sorted([nums[i], nums[j], nums[k]]))
        return result
