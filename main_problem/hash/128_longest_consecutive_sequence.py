class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        result = 0
        sequence = 1
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif nums[i] + 1 == nums[i + 1]:
                sequence += 1
            else:
                result = max(result, sequence)
                sequence = 1
        return max(result, sequence)
