import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        s = list(s)
        r = math.ceil(len(s)/(2*numRows-2)) + 1
        zz = [['' for _ in range(r+(numRows-2)*(r-1))] for _ in range(numRows)]
        p, i, j = 0, 0, 0
        while p < len(s):
            for i in range(numRows):
                zz[i][j] = s[p]
                p += 1
                if p == len(s):
                    break
            if p == len(s):
                break

            for z in range(numRows-2):

                j = j + 1
                i -= 1
                zz[i][j] = s[p]
                p += 1
                if p == len(s):
                    break
            i -= 1
            j += 1

        for i in range(len(zz)):
            zz[i] = ''.join(zz[i])
        return ''.join(zz)
