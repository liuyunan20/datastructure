class Solution:
    def myPow_tle(self, x: float, n: int) -> float:
        res = 1
        if x == 0:
            return x
        if n == 0:
            return 1
        if n > 0:
            for _ in range(n):
                res *= x
        if n < 0:
            for _ in range(-n):
                res /= x
        return res
