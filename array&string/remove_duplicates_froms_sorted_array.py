from typing import List


class Solution:
    def removeDuplicates_slow(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = None
        while None in nums:
            nums.remove(None)
        return len(nums)

    def removeDuplicates_faster(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = float('inf')
                k += 1
        nums.sort()
        return len(nums) - k

    # faster than above 2
    def removeDuplicates_2pointers(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i + 1] = nums[j]
                i += 1
        return i + 1
