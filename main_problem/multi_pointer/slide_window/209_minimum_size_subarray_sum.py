from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = [0]
        i = j = s = 0
        n = len(nums)
        while j < n:
            s += nums[j]
            if s < target:
                j += 1
            else:
                while i < n and s - nums[i] >= target:
                    s -= nums[i]
                    i += 1
                result.append(j - i + 1)
                j += 1
        result.sort()
        return result[1] if len(result) > 1 else 0
