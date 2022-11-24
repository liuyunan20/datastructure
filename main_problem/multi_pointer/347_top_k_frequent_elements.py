from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq.setdefault(num, 0)
            freq[num] += 1
        result = sorted(freq.items(), key=lambda x: -x[1])
        return [result[i][0] for i in range(k)]
