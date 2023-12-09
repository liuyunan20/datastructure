class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
        new = ''
        for i in range(len(num)):
            if num[i] == '1':
                new += '0'
            if num[i] == '0':
                new += '1'
        print(new)
        return int(new, 2)
