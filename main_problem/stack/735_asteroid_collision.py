from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for ast in asteroids:
            if not result or ast > 0:
                result.append(ast)
            elif result and ast < 0:
                explode = ast
                while result and 0 < result[-1] < -ast:
                    result.pop()
                if not result:
                    result.append(ast)
                elif result[-1] == -ast:
                    result.pop()
                elif result[-1] < 0:
                    result.append(ast)

        return result
