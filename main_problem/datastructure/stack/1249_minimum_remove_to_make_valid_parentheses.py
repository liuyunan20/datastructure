class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_list = list(s)
        stack = []
        i = 0
        while s_list:
            element = s_list.pop(0)
            if element == "(":
                stack.append((element, i))
            if element == ")" and stack and stack[-1][0] == "(":
                stack.pop()
                i += 1
                continue
            if element == ")" and (not stack or stack[-1][0] != "("):
                stack.append((element, i))
            i += 1
        s_list = list(s)
        for element, i in stack:
            s_list[i] = ""
        return "".join(s_list)
