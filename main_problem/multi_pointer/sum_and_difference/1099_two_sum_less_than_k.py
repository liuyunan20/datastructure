class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        s = -1
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < k:
                    s = max(s, nums[i] + nums[j])
        return s
