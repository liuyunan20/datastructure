class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while i <= n:
            n -= i
            i += 1
        return i - 1
