from typing import List


class Solution:
    def numSubarrayProductLessThanK_tle(self, nums: List[int], k: int) -> int:
        def product(arr):
            pro = 1
            for num in arr:
                pro *= num
            return pro

        i = 0
        n = len(nums)
        result = 0
        while i < n:
            window = 0
            while i + window < n:
                if product(nums[i: i + window + 1]) < k:
                    result += 1
                    window += 1
                else:
                    break
            i += 1
        return result
