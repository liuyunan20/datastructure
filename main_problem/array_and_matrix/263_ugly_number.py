class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            nc = n
            if n / 2 == n // 2:
                n = n // 2
            if n / 3 == n // 3:
                n = n // 3
            if n / 5 == n // 5:
                n = n // 5
            if nc == n:
                return False
        return True
