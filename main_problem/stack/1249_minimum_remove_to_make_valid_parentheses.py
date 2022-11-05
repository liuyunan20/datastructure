class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        l = len(s)
        i = 0
        delete = []
        while i < l:
            if s[i] != ')':
                stack.append((s[i], i))
            else:
                if stack:
                    element = stack.pop()
                    while stack and element[0] in string.ascii_lowercase:
                        element = stack.pop()

                    if element[0] != '(' and not stack:
                        delete.append((s[i], i))
                    elif element[0] == ')':
                        delete.append(element)
                else:
                    delete.append((s[i], i))
            i += 1
        for element in stack:
            if element[0] in ['(', ')']:
                delete.append(element)
        result = ''
        position = [e[1] for e in delete]
        for i in range(l):
            if i not in position:
                result = result + s[i]
        return result
