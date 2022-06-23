class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target == nums[-1]:
            return len(nums) - 1
        for i in range(len(nums) - 1):
            if nums[i] == target:
                return i
            if nums[i] < target < nums[i+1]:
                return i + 1
