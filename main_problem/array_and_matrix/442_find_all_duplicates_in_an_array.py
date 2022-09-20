from _ast import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        num_freq = {}
        result = []
        for num in nums:
            num_freq.setdefault(num, 0)
            num_freq[num] += 1
            if num_freq[num] == 2:
                result.append(num)
        return result
