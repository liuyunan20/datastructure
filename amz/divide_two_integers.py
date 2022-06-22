class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = True
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            positive = False
        max_int = 2147483647
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor == 1:
            counter = dividend
        result = 0
        while dividend >= divisor:
            counter = 0
            divisor_copy = divisor
            while dividend >= divisor_copy:
                root = divisor_copy
                divisor_copy += divisor_copy
                counter += 1
            divisor_copy -= root
            counter -= 1
            result += 2 ** counter
            dividend -= divisor_copy
        if positive:
            if result > max_int:
                return max_int
            return result
        else:
            return -result
