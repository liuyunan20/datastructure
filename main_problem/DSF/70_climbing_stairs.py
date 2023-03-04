class Solution:
    def climbStairs_tle(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = self.climbStairs(n - 1)
        b = self.climbStairs(n - 2)
        return a + b
