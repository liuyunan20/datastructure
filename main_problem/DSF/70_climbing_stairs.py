class Solution:
    def climbStairs(self, n: int) -> int:
        result = [1, 2]
        for i in range(2, n):
            result.append(result[i - 1] + result[i - 2])
        return result[n - 1]
