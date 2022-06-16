class Solution:
    def romanToInt(self, s: str) -> int:
        s = s[::-1]
        i = 0
        num = 0
        l = len(s) - 1
        s_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}
        if l == 0:
            return s_value[s]
        while i < l:
            if s[i] == 'I':
                num += 1
                i += 1
            elif s[i] == 'V':
                if s[i+1] == 'I':
                    num += 4
                    i += 2
                else:
                    num += 5
                    i += 1
            elif s[i] == 'X':
                if s[i+1] == 'I':
                    num += 9
                    i += 2
                else:
                    num += 10
                    i += 1
            elif s[i] == 'L':
                if s[i+1] == 'X':
                    num += 40
                    i += 2
                else:
                    num += 50
                    i += 1
            elif s[i] == 'C':
                if s[i+1] == 'X':
                    num += 90
                    i += 2
                else:
                    num += 100
                    i += 1
            elif s[i] == 'D':
                if s[i+1] == 'C':
                    num += 400
                    i += 2
                else:
                    num += 500
                    i += 1
            elif s[i] == 'M':
                if s[i+1] == 'C':
                    num += 900
                    i += 2
                else:
                    num += 1000
                    i += 1

        if s[-1] == 'M':
            num += 1000
        if s[-1] == 'D':
            num += 500
        if s[-2] != 'M' and s[-2] != 'D' and s[-1] == 'C':
            num += 100
        if s[-1] == 'L':
            num += 50
        if s[-2] != 'C' and s[-2] != 'L' and s[-1] == 'X':
            num += 10
        if s[-1] == 'V':
            num += 5
        if s[-2] != 'V' and s[-2] != 'X' and s[-1] == 'I':
            num += 1
        return num

    def romanToInt_better(self, s: str) -> int:
        s_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}
        s = s[::-1]
        i = 1
        num = s_value[s[0]]

        while i < len(s):
            if s_value[s[i]] < s_value[s[i-1]]:
                num -= s_value[s[i]]
            else:
                num += s_value[s[i]]
            i += 1
        return num
