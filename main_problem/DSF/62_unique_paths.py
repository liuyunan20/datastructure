class Solution:
    def uniquePaths_tle(self, m: int, n: int) -> int:

        def helper(i, j, path):
            paths = []

            def helper(i, j):
                if i == m - 1 or j == n - 1:
                    paths.append(1)
                    return
                else:
                    helper(i + 1, j)
                    helper(i, j + 1)

            helper(0, 0)
            return len(paths)

