from typing import List


class Solution:
    def maxSlidingWindow_tle(self, nums: List[int], k: int) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n - k + 1):
            result.append(max(nums[i: i + k]))
        return result

    def maxSlidingWindow_tle2(self, nums: List[int], k: int) -> List[int]:
        result = []
        n = len(nums)
        max_num = max(nums[:k])
        result.append(max_num)
        for i in range(k, n):
            if nums[i] >= max_num:
                result.append(nums[i])
                max_num = nums[i]
            elif nums[i - k] == max_num:
                max_num = max(nums[i - k + 1: i + 1])
                result.append(max_num)
            else:
                result.append(max_num)
        return result
