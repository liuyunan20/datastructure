class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': ')', '[': ']', '{': '}'}
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] in mapping:
                stack.append(s[i])
            else:
                if stack and mapping[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
        return not stack
