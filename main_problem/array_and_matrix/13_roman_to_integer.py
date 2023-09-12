class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s[::-1]
        n = len(s)
        i = 0
        result = 0
        while i < n:
            if i + 1 < n and roman[s[i]] > roman[s[i + 1]]:
                result += roman[s[i]] - roman[s[i + 1]]
                i += 2
            else:
                result += roman[s[i]]
                i += 1
        return result
