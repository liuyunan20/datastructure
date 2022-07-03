from typing import List


class Solution:
    def findMissingRanges_tle(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        j = i = lower
        while i <= upper:
            while i not in nums and i <= upper:
                i += 1
            if i > j:
                result.append([j, i-1])
            while i in nums:
                i += 1
                j = i
        for i, el in enumerate(result):
            if el[0] == el[1]:
                result[i] = str(el[0])
            else:
                result[i] = str(el[0]) + '->' + str(el[1])
        return result
