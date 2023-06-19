class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        sub_sum = 0
        i = 0
        n = len(nums)
        while i < n:
            if sub_sum == total - sub_sum - nums[i]:
                return i
            sub_sum += nums[i]
            i += 1
        return -1
