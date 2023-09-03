from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(key=lambda x: -x)
        i = 0
        n = len(citations)
        while i < n:
            if citations[i] >= i + 1:
                i += 1
            else:
                break
        return i
