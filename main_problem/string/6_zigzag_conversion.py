class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = []
        for j in range(numRows):
            i = j
            while i < len(s):
                result.append(s[i])
                if j not in [0, numRows - 1]:
                    m = i + numRows - (j + 1) + numRows - 2 - (j - 1)
                    if m < len(s):
                        result.append(s[m])
                i = i + 2 * numRows - 2
        return ''.join(result)
