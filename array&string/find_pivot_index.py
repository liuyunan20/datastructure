class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_left = 0
        sum_right = sum(nums[1:])
        for i, num in enumerate(nums):
            if sum_left == sum_right:
                return i
            if i < len(nums) - 1:
                sum_left += num
                sum_right -= nums[i + 1]
        return -1
