from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        i = 0
        j = 0
        result = []
        while i < len(nums) - 1:
            if nums[i] != nums[i+1] - 1:
                if i == j:
                    result.append(str(nums[i]))
                else:
                    result.append(str(nums[j]) + '->' + str(nums[i]))
                j = i + 1
            i += 1
        if nums[-1] == nums[-2] + 1:
            result.append(str(nums[j]) + '->' + str(nums[-1]))
        else:
            result.append(str(nums[-1]))
        return result
