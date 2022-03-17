class Solution:
    def numSquares(self, n: int) -> int:
        square = [x**2 for x in range(1, 101)]
        queue = [n]
        step = 0
        while queue:
            next_step = []
            step += 1
            for n in queue:
                for s in square:
                    if s == n:
                        return step
                    elif n - s > 0:
                        next_step.append(n - s)
            queue = next_step
