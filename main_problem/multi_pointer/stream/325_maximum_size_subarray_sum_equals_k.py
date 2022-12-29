from typing import List


class Solution:
    def maxSubArrayLen_tle(self, nums: List[int], k: int) -> int:
        n = len(nums)
        length = 0
        i = 0
        while i < n:
            sub_sum = 0
            j = i
            while j < n:
                sub_sum += nums[j]
                if sub_sum == k:
                    length = max(length, j - i + 1)
                j += 1
            i += 1
        return length
    def maxSubArrayLen_tle2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        length = 0
        i = 0
        j = n - 1
        sub_sum = sum(nums)
        while i <= j:
            current_sum = sub_sum
            while j >= i:
                if current_sum == k:
                    length = max(length, j - i + 1)
                    break
                current_sum -= nums[j]
                j -= 1
            j = n - 1
            sub_sum -= nums[i]
            i += 1
        return length
