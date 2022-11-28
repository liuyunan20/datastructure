class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        i = n1 - 1
        result = []
        product = 0
        while i >= 0:
            j = n2 - 1
            while j >= 0:
                product += int(num1[i]) * int(num2[j]) * 10 ** (n1 - 1 - i) * 10 ** (n2 - 1 - j)
                j -= 1
            i -= 1
        return str(product)
