class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        start = 0
        end = x
        while start <= end:
            i = (end - start) // 2 + start
            p = i * i
            if p == x:
                return i
            elif p < x:
                start = i + 1
            else:
                end = i - 1
        return end
