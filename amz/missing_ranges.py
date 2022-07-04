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

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        if not nums:
            if lower != upper:
                return [str(lower) + '->' + str(upper)]
            return [str(lower)]
        if lower != nums[0]:
            result.append([lower, nums[0]-1])
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1] - 1:
                result.append([nums[i]+1, nums[i+1]-1])
        if upper != nums[-1]:
            result.append([nums[-1]+1, upper])

        for i, el in enumerate(result):
            if el[0] == el[1]:
                result[i] = str(el[0])
            else:
                result[i] = str(el[0]) + '->' + str(el[1])
        return result
