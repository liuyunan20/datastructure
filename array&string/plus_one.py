from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        num = 0
        for i, digit in enumerate(digits):
            num += digit * 10 ** (l - 1 - i)
        num += 1
        digits = [int(x) for x in list(str(num))]
        return digits
