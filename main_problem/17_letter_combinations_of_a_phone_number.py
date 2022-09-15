from _ast import List


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
        if not digits:
            return []
        result = []
        def backtrack(i, current):
            if i == len(digits):
                result.append(''.join(current))
                return
            for j in range(len(digit_letter[digits[i]])):
                current.append(digit_letter[digits[i]][j])
                backtrack(i+1, current)
                current.pop()
        backtrack(0, [])
        return result
