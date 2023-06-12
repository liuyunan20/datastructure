from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        for num in nums:
            freq.setdefault(num, 0)
            freq[num] += 1
        result = 0
        for num in freq:
            if num != k - num and freq.get(k - num):
                d = min(freq[num], freq[k - num])
                result += d
                freq[num] -= d
                freq[k - num] -= d
            if num == k - num:
                d = freq[num] // 2
                result += d
        return result
