class Solution:
    def romanToInt(self, s: str) -> int:
        s = s[::-1]
        i = 0
        result = 0
        length = len(s)
        while i < length:
            if s[i] == "I":
                result += 1
                i += 1
                continue
            if s[i] == "V":
                if i + 1 < length and s[i + 1] == "I":
                    result += 4
                    i += 2
                else:
                    result += 5
                    i += 1
                continue
            if s[i] == "X":
                if i + 1 < length and s[i + 1] == "I":
                    result += 9
                    i += 2
                else:
                    result += 10
                    i += 1
                continue
            if s[i] == "L":
                if i + 1 < length and s[i + 1] == "X":
                    result += 40
                    i += 2
                else:
                    result += 50
                    i += 1
                continue
            if s[i] == "C":
                if i + 1 < length and s[i + 1] == "X":
                    result += 90
                    i += 2
                else:
                    result += 100
                    i += 1
                continue
            if s[i] == "D":
                if i + 1 < length and s[i + 1] == "C":
                    result += 400
                    i += 2
                else:
                    result += 500
                    i += 1
                continue
            if s[i] == "M":
                if i + 1 < length and s[i + 1] == "C":
                    result += 900
                    i += 2
                else:
                    result += 1000
                    i += 1
                continue
        return result

    def romanToInt_2(self, s: str) -> int:
        s = s[::-1]
        length = len(s)
        result = 0
        i = 0
        roman_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        while i < length:
            if i + 1 < length and roman_int[s[i]] > roman_int[s[i + 1]]:
                result += roman_int[s[i]] - roman_int[s[i + 1]]
                i += 2
            else:
                result += roman_int[s[i]]
                i += 1
        return result
