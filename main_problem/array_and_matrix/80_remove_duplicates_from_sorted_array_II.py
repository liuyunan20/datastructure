from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        k = 0
        for i in range(n):
            freq.setdefault(nums[i], 0)
            if freq[nums[i]] < 2:
                freq[nums[i]] += 1
            else:
                nums[i] = 10001
                k += 1
        nums.sort()
        return n - k
