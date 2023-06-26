import string

import int as int


class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        i = 0
        stack = []
        while i < n:
            if s[i] == ']':
                repeat = ''
                while stack[-1] != '[':
                    repeat += stack.pop()
                stack.pop()
                num = ''
                while stack and stack[-1] in string.digits:
                    num += stack.pop()
                stack += list(repeat[::-1] * int(num[::-1]))
            else:
                stack.append(s[i])
            i += 1
        return ''.join(stack)
