class Solution:
    def romanToInt(self, s: str) -> int:
        i = len(s) - 1
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        while i >= 0:
            if i - 1 >= 0 and mapping[s[i - 1]] < mapping[s[i]]:
                result += mapping[s[i]] - mapping[s[i - 1]]
                i -= 2
            else:
                result += mapping[s[i]]
                i -= 1

        return result
