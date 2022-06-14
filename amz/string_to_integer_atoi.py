import string


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        if s[0] not in ['+', '-']:
            s = '+' + s
        if len(s) == 1 or s[1] not in string.digits:
            return 0
        i = 2
        while i < len(s) and s[i] in string.digits:
            i += 1
        x = int(s[:i])
        if x > 2147483647:
            return 2147483647
        if x < -2147483648:
            return -2147483648
        else:
            return x
