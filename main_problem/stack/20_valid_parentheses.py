class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        i = 0
        stack = []
        pairs = {'}': '{', ']': '[', ')': '('}
        while i < length:
            if s[i] in pairs:
                if not stack:
                    return False
                elif pairs[s[i]] != stack.pop():
                    return False
            else:
                stack.append(s[i])
            i += 1
        return True if not stack else False
