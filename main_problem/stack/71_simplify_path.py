class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        i = 0
        stack = []
        period = ''
        while i < n:
            while i < n and path[i] == '.':
                period += path[i]
                i += 1
            if period == '..' and stack[-1] == '/' and (i == n or path[i] == '/'):
                stack.pop()
                while stack and stack[-1] != '/':
                    stack.pop()
                period = ''
                continue
            if period == '.' and stack[-1] == '/' and (i == n or path[i] == '/'):
                period = ''
                continue
            if period:
                stack.append(period)
            period = ''
            if i == n:
                break
            if path[i] == '/' and stack and stack[-1] == '/':
                i += 1
                continue
            else:
                stack.append(path[i])
                i += 1
        if len(stack) > 1 and stack[-1] == '/':
            stack.pop()
        if not stack:
            stack.append('/')
        return ''.join(stack)
