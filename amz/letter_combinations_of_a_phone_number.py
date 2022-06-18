import itertools
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_letter = {'2': ['a', 'b', 'c'],
                        '3': ['d', 'e', 'f'],
                        '4': ['g', 'h', 'i'],
                        '5': ['j', 'k', 'l'],
                        '6': ['m', 'n', 'o'],
                        '7': ['p', 'q', 'r', 's'],
                        '8': ['t', 'u', 'v'],
                        '9': ['w', 'x', 'y', 'z']}
        letters = []
        result = set()
        if not digits:
            return list(result)
        for i in list(digits):
            letters.append(digit_letter[i])
        for element in itertools.product(*letters):
            result.add(''.join(element))
        return list(result)
