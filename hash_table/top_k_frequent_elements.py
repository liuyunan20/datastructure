from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            num_freq.setdefault(num, 0)
            num_freq[num] += 1
        sorted_freq = sorted(num_freq.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_freq[i][0])
        return result
