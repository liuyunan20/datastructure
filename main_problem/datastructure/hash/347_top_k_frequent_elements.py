from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq.setdefault(num, 0)
            freq[num] += 1
        nums = sorted(freq.items(), key=lambda x: -x[1])
        result = []
        for i in range(k):
            result.append(nums[i][0])
        return result
