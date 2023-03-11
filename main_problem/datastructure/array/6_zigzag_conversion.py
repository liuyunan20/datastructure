class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        i = 0
        zigzag = []
        while i < n:
            col = list(s[i: i + numRows])
            if len(col) != numRows:
                col += [0 for _ in range(numRows - len(col))]
            zigzag.append(col)
            i += numRows
            if i < n:
                for j in range(numRows - 2):
                    if i >= n:
                        break
                    col = [0 for _ in range(numRows)]
                    col[numRows - j - 2] = s[i]
                    zigzag.append(col)
                    i += 1
        print(zigzag)
        result = ''
        for i in range(numRows):
            for x in zigzag:
                if x[i] != 0:
                    result += x[i]
        return result
