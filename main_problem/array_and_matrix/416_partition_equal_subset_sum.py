class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        i = 0
        n = len(nums)
        while i < n:
            if sum(nums[:i]) == sum(nums[i:]):
                return True
            i += 1
        return False
