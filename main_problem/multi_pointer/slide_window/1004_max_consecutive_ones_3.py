from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        j = 0
        counter = nums[0]
        result = counter if n > 1 else max(counter, n)
        while j < n:
            if j - i + 1 - counter <= k:
                if j + 1 < n:
                    counter += nums[j + 1]
                j += 1
            else:
                counter -= nums[i]
                i += 1
            result = max(result, j - i)
        return result
