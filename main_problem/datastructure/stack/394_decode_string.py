import string


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        s = list(s)
        while s:
            symbol = s.pop(0)
            if symbol != "]":
                stack.append(symbol)
            else:
                sub = []
                while stack[-1] != "[":
                    sub.append(stack.pop())
                stack.pop()
                num = ""
                while stack and stack[-1] in string.digits:
                    num += stack.pop()
                for _ in range(int(num[::-1])):
                    stack += sub[::-1]
        return "".join(stack)
