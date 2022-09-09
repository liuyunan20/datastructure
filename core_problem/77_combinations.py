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
