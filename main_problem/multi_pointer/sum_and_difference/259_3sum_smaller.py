from typing import List


class Solution:
    def threeSumSmaller_tle(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] < target:
                        result += 1
        return result

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] < target:
                        result += 1
                    else:
                        break
        return result
