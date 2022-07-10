class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = n // 2 ** (31 - i)
            n -= bit * 2 ** (31 - i)
            if bit == 1:
                result += 1
        return result
