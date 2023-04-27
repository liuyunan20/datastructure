class Solution:
    def uniquePaths_tle(self, m: int, n: int) -> int:

        def helper(i, j, path):
            if i == m - 1 and j == n - 1:
                return path + 1
            elif i == m - 1:
                path = helper(i, j + 1, path)
            elif j == n - 1:
                path = helper(i + 1, j, path)
            else:
                path = helper(i + 1, j, path) + helper(i, j + 1, path)
            return path

        return helper(0, 0, 0)

