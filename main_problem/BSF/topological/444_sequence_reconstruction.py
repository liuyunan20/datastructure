from typing import List


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        pre_num = {}
        def find_pre(arr):
            if len(arr) > 1:
                for i in range(1, len(arr)):
                    pre_num.setdefault(arr[i], set()).add(arr[i - 1])
        for seq in sequences:
            find_pre(seq)
        if nums[0] in pre_num:
            return False
        for i in range(1, len(nums)):
            if nums[i] not in pre_num:
                return False
            if nums[i - 1] not in pre_num[nums[i]]:
                return False
        return True
