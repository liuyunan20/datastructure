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
