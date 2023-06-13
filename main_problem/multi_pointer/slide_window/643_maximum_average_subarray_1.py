class Solution:
    def findMaxAverage_tle(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if k == 1:
            return max(nums)
        i = 0
        result = -2147483648
        while i <= n - k:
            result = max(result, sum(nums[i: i + k]) / k)
            i += 1
        return result
