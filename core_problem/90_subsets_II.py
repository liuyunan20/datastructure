from _ast import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(i, current):
            if i == len(nums):
                result.append(list(current))
                return
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, current)

        backtrack(0, [])
        return result
