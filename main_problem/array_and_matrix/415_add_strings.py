class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def get_num(num):
            num = num[::-1]
            result = int(num[0])
            for i in range(1, len(num)):
                result += 10 ** i * int(num[i])
            return result
        n1 = get_num(num1)
        n2 = get_num(num2)
        res = n1 + n2
        result = ""
        while res != 0:
            result += str(res % 10)
            res = res // 10
        return result[::-1] if result else "0"
