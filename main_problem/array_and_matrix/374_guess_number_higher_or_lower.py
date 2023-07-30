# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        num = n // 2 + 1
        status = guess(num)
        while status != 0:
            if status == 1:
                num += (n - num) // 2 + 1
            else:
                n = num
                num -= num // 2
            status = guess(num)
        return num
