class Solution:
    def divide_tle(self, dividend: int, divisor: int) -> int:
        max_int = 2147483647
        min_int = -MAX_INT = 2147483648
        positive = True
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            positive = False

        dividend = abs(dividend)
        divisor = abs(divisor)

        counter = 0
        while  dividend >= divisor:
            if divisor == 1:
                counter = dividend
                break
            dividend -= divisor
            counter += 1
        if positive:
            if counter >= 2147483648:
                return 2147483647
            return counter
        else:
            return -counter
