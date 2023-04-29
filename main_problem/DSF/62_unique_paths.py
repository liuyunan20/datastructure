class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def helper(i, j, path):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == m - 1 or j == n - 1:
                memo[(i, j)] = path + 1
                return path + 1
            else:
                path = helper(i + 1, j, path) + helper(i, j + 1, path)
                memo[(i, j)] = path
                return path

        return helper(0, 0, 0)

