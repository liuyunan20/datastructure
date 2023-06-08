class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = list(str(num))
            s = 0
            for d in num:
                s += int(d)
            num = s
        return num
