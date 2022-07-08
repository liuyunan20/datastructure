import string


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 1
        letter_num = {}
        for letter in string.ascii_uppercase:
            letter_num[letter] = num
            num += 1
        ct = columnTitle[::-1]
        num = 0
        for i in range(len(ct)):
            num += 26 ** i * letter_num[ct[i]]
        return num
