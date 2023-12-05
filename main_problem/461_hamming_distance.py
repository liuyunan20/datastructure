class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = str(bin(x)[2:])
        y = str(bin(y)[2:])
        print(x, y)
        nx = len(x) - 1
        ny = len(y) - 1
        result = 0
        while nx >= 0 or ny >= 0:
            a = x[nx] if nx >= 0 else '0'
            b = y[ny] if ny >= 0 else '0'
            if a != b:
                result += 1
            nx -= 1
            ny -= 1
        return result
