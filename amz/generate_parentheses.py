from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        result = set()
        for pairs in self.generateParenthesis(n-1):
            for i in range(len(pairs)):
                p = list(pairs)
                p.insert(i, '()')
                p = ''.join(p)
                result.add(p)
        return result
