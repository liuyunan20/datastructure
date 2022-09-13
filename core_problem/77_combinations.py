from _ast import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(first, current):
            if len(current) == k:
                result.append(list(current))
            for i in range(first, n + 1):
                current.append(i)
                backtrack(i + 1, current)
                current.pop()

        backtrack(1, [])
        return result

    def combine_2(self, n: int, k: int) -> List[List[int]]:
        result = []
        # use index to explore all numbers, append appropriate current list to result
        # for each index, the current list could include it or not include
        def backtrack(i, current):
            if len(current) == k:
                result.append(list(current))
                return
            if i == n + 1:
                return
            current.append(i)
            backtrack(i + 1, current)
            current.pop()

            backtrack(i + 1, current)

        backtrack(1, [])
        return result
