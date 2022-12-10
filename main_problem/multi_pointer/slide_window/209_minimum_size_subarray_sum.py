from typing import List


class Solution:
    def minSubArrayLen_tle(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        i = 0
        j = 0
        result = len(nums)
        while j < len(nums):
            if sum(nums[i: j + 1]) < target:
                j += 1
            else:
                result = min(result, j - i + 1)
                i += 1
        return result

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        i = 0
        j = 0
        n = len(nums)
        result = n
        sub_sum = 0
        while j <= n:
            if sub_sum < target and j < n:
                sub_sum += nums[j]
                j += 1
            elif sub_sum >= target:
                result = min(result, j - i)
                sub_sum -= nums[i]
                i += 1
            else:
                break
        return result
