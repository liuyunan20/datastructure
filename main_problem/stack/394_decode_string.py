import string

import int as int


class Solution:
    def decodeString(self, s: str) -> str:
        l = len(s)
        i = 0
        stack = []
        while i < l:
            if s[i] == "]":
                temporary = ""
                letter = stack.pop()
                while letter != "[":
                    temporary = letter + temporary
                    letter = stack.pop()

                number = ""
                digit = stack.pop()
                while digit and digit in string.digits:
                    number += digit
                    if stack:
                        digit = stack.pop()
                    else:
                        digit = ""
                stack.append(digit)
                number = int(number[::-1])
                stack.append(temporary * number)
            else:
                stack.append(s[i])
            i += 1
        return "".join(stack)
