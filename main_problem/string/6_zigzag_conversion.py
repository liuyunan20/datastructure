class Solution:
    class Solution:
        def convert(self, s: str, numRows: int) -> str:
            result = [[] for _ in range(numRows)]
            i = 0
            n = len(s)
            middle = []
            col = 0
            while i < n:
                for j in range(numRows):
                    if i < n:
                        result[j].append(s[i])
                        i += 1
                    else:
                        break
                col += 1
                for _ in range(1, numRows - 1):
                    for j in range(numRows):
                        if i >= n:
                            break
                        elif numRows - 1 - j == col % (numRows - 1):
                            result[j].append(s[i])
                            i += 1
                        else:
                            result[j].append('')
                    col += 1

            for i in range(numRows):
                result[i] = ''.join(result[i])
            return ''.join(result)

