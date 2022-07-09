class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        for i in range(32):
            bit = n // (2 ** (31-i))
            bits.append(bit)
            n -= bit * 2 ** (31-i)
        bits = bits[::-1]
        result = 0
        for i in range(32):
            result += bits[i] * 2 ** (31-i)
        return result
