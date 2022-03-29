class Solution:
    def addBinary(self, a: str, b: str) -> str:
        helper_value = {0: ('0', '0'), 1: ('0', '1'), 2: ('1', '0'), 3: ('1', '1')}
        a_list = list(a)
        b_list = list(b)
        length = max(len(a), len(b))
        if len(a) > len(b):
            b_list = [0] * (length - len(b)) + b_list
        if len(a) < len(b):
            a_list = [0] * (length - len(a)) + a_list
        helper = 0
        result = []
        for i in range(length - 1, -1, -1):
            helper, value = helper_value[int(a_list[i]) + int(b_list[i]) + int(helper)]
            result.append(value)
        if helper == '1':
            result.append('1')
        return "".join(result[::-1])
