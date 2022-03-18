from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operation(a, b, oper):
            if oper == '+':
                return a + b
            if oper == '-':
                return a - b
            if oper == '*':
                return a * b
            if oper == '/' and b != 0:
                return a / b
            if oper == '/' and b == 0:
                print('Invalid 0 divider')
                return None

        stack = []
        for element in tokens:
            if element in ('+', '-', '*', '/'):
                b = stack.pop()
                a = stack.pop()
                result = operation(int(a), int(b), element)
                stack.append(result)
            else:
                stack.append(element)
        return int(stack[0])
