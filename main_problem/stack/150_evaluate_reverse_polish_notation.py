from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def op(x, y, operation):
            if operation == '+':
                return x + y
            if operation == '-':
                return x - y
            if operation == '*':
                return x * y
            if operation == '/':
                if x == 0:
                    return 0
                return (abs(x) // abs(y)) * (x // abs(x)) * (y // abs(y))
        n = len(tokens)
        stack = []
        operation = ['+', '-', '*', '/']
        for i in range(n):
            if tokens[i] in operation:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(op(b, a, tokens[i]))
            else:
                stack.append(tokens[i])
        return int(stack[0])
