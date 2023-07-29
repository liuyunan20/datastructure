class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 0
        n = 0
        while n < num:
            n = i * i
            i += 1
        return n == num
