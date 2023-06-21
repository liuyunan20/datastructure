from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for num in arr:
            freq.setdefault(num, 0)
            freq[num] += 1
        return len(freq) == len(set(freq.values()))
