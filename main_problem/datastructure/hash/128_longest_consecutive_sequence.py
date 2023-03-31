from typing import List


class Solution:
    def longestConsecutive_tle(self, nums: List[int]) -> int:
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

    def longestConsecutive(self, nums: List[int]) -> int:
        number = set(nums)
        result = 0
        visited = set()
        for num in nums:
            if num in visited:
                continue
            i = 1
            counter = 1
            while num + i in number:
                visited.add(num + i)
                counter += 1
                i += 1
            i = 1
            while num - i in number:
                visited.add(num - i)
                counter += 1
                i += 1
            result = max(result, counter)
        return result
