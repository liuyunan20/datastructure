class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_list = list(s)
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                stack.append((s[i], i))
            elif s[i] == ")" and stack and stack[-1][0] == "(":
                stack.pop()
            elif s[i] == ")" and (not stack or stack[-1][0] != "("):
                stack.append((s[i], i))
            i += 1
        for element, i in stack:
            s_list[i] = ""
        return "".join(s_list)
