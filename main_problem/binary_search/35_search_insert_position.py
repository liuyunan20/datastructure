class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)
        while i < j:
            n = (i + j) // 2
            if target == nums[n]:
                return n
            elif target > nums[n]:
                i = n + 1
            else:
                j = n - 1
        if j < 0:
            return 0
        if i == len(nums):
            return len(nums)
        return i if target <= nums[i] else i + 1
