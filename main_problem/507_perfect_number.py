class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = []
        s = 1
        l = num
        i = 2
        first = True
        while i < l:
            if num / i == num // i:
                s += i
                if first:
                    l = num // i + 1
                    first = False
            i += 1
        return s == num
