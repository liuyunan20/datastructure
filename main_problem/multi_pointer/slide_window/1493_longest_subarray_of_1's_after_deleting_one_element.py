from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        i = 0
        j = 0
        counter = nums[0]
        result = counter
        while j < n:
            if j + 1 - i - counter <= 1:
                if j + 1 < n:
                    counter += nums[j + 1]
                j += 1
            else:
                counter -= nums[i]
                i += 1
            result = max(result, j - i - 1)
        return result
