from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        result = []
        for num in nums:
            freq.setdefault(num, 0)
            freq[num] += 1
            if freq[num] == 2:
                result.append(num)
        return result
