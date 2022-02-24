class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        s_pair = {"(": ")", "[": "]", "{": "}", "0": "0"}
        open_p = ("(", "[", "{")
        s_stack = ["0"]

        for i in range(len(s_list)):
            if s_list[i] in open_p:
                s_stack.append(s_list[i])
            else:
                if s_pair[s_stack[-1]] != s_list[i]:
                    return False
                else:
                    s_stack.pop(-1)
        if len(s_stack) > 1:
            return False
        else:
            return True
