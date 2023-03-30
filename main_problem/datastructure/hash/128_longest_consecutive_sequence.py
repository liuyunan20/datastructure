from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number = {}
        result = 0
        for num in nums:
            number.setdefault(num, 0)
            number[num] += 1
        for num in nums:
            i = 1
            counter = 1
            while number.get(num + i):
                counter += 1
                i += 1
            i = 1
            while number.get(num - i):
                counter += 1
                i += 1
            result = max(result, counter)
        return result
