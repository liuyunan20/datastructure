class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        visited = {n, }
        while True:
            n = list(str(n))
            s = 0
            for digit in n:
                s += int(digit) ** 2
            n = s
            if n in visited:
                return False
            if n == 1:
                return True
            visited.add(n)
