from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        l = len(nums)
        if l % 2 == 1:
            return nums[int((l-1)/2)]
        else:
            return (nums[int(l/2)]+nums[int(l/2-1)])/2
