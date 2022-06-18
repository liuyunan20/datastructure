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

    # sort all numbers and don't accept the number smaller than current two numbers
    # to avoid duplicate triplets
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_pst = {}
        result = []
        for num in nums:
            num_pst.setdefault(num, 0)
            num_pst[num] += 1

        nums = list(num_pst.keys())
        length = len(nums)
        if num_pst.get(0) and num_pst[0] > 2:
            result.append([0, 0, 0])
        for i in range(length):
            for j in range(i+1, length):
                s = -nums[i] - nums[j]
                if num_pst.get(s) is not None:
                    if ((nums[i] == s or nums[j] == s) and num_pst[s] > 1) or (nums[i] < s and nums[j] < s):
                        result.append([nums[i], nums[j], s])
        return result
