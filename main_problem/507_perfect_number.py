class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        s = 1
        i = 2
        first = True
        while i < int(num ** 0.5) + 1:
            if num / i == num // i:
                s += i + num // i
            i += 1
        return s == num
