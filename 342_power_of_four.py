class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False
        while n > 1 and n == int(n):
            n /= 4
        return n == 1
