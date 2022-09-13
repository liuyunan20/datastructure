from _ast import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(first, current):
            if len(current) == k:
                result.append(list(current))
                return
            for i in range(first, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        for k in range(len(nums) + 1):
            backtrack(0, [])
        return result

    def subsets_2(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(i, current):
            if i == len(nums):
                result.append(list(current))
                return

            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

            backtrack(i + 1, current)

        backtrack(0, [])
        return result
