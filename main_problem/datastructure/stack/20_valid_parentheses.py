class Solution:
    def isValid(self, s: str) -> bool:
        left_right = {'(': ')', '[': ']', '{': '}'}
        stack = []
        s = list(s)
        while s:
            cur = s.pop(0)
            if cur in left_right:
                stack.append(cur)
            elif not stack or left_right[stack[-1]] != cur:
                return False
            else:
                stack.pop()
        if not stack:
            return True
        return False
