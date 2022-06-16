class Solution:
    def intToRoman(self, num: int) -> str:
        num_str = ''
        m = num // 1000
        num_str += 'M' * m
        num = num % 1000
        if num >= 900:
            num_str += 'CM'
            num -= 900
        else:
            d = num // 500
            num_str += 'D' * d
            num = num % 500
        if num >= 400:
            num_str += 'CD'
            num -= 400
        else:
            c = num // 100
            num_str += 'C' * c
            num = num % 100
        if num >= 90:
            num_str += 'XC'
            num -= 90
        else:
            l = num // 50
            num_str += 'L' * l
            num = num % 50
        if num >= 40:
            num_str += 'XL'
            num -= 40
        else:
            x = num // 10
            num_str += 'X' * x
            num = num % 10
        if num == 9:
            num_str += 'IX'
            num -= 9
        else:
            v = num // 5
            num_str += 'V' * v
            num = num % 5
        if num == 4:
            num_str += 'IV'
        else:
            num_str += 'I' * num
        return num_str
