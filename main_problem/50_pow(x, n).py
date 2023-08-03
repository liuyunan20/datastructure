class Solution:
    def myPow_tle(self, x: float, n: int) -> float:
        if x == 0:
            return x
        if n == 0:
            return 1
        if n > 0:
            return self.myPow(x, n - 1) * x
        if n < 0:
            return self.myPow(x, n + 1) / x
