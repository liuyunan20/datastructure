from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 1
        first = True
        cur = nums[i]
        while j < n:
            if nums[i] == nums[j]:
                if first:
                    nums[i + 1] = nums[j]
                    j += 1
                    i += 1
                    first = False
                else:
                    j += 1
            else:
                nums[i + 1] = nums[j]
                i += 1
                j += 1
                first = True
        return i + 1
