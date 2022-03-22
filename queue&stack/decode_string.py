import string


class Solution:
    def decodeString(self, s: str) -> str:
        s_list = list(s)
        stack = []

        for x in s_list:
            letters = []
            num = ""
            if x == "]":
                while stack[-1] != "[":
                    letters.append(stack.pop())
                letters = reversed(letters)
                stack.pop()
                while stack and stack[-1] in string.digits:
                    num += stack.pop()
                stack.append(int(num[::-1]) * "".join(letters))
            else:
                stack.append(x)
        return "".join(stack)
