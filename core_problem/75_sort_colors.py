from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def helper(left, right, color):
            while left <= right:
                while left <= right and nums[left] == color:
                    left += 1
                while left <= right and nums[right] >= color+1:
                    right -= 1
                while left <= right and nums[right] == color:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
            return left

        l = helper(0, len(nums)-1, 0)
        helper(l, len(nums)-1, 1)

    def sortColors_quicksort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1
