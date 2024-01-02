class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        sl = len(s)
        new = []
        for i in range(sl):
            if s[i] != '-':
                new.append(s[i])
        sl = len(new)
        first_group_len = sl % k
        result = []
        group = ''
        if first_group_len > 0:
            for _ in range(first_group_len):
                group += new.pop(0).upper()
            result.append(group)
        while new:
            group = ''
            for _ in range(k):
                group += new.pop(0).upper()
            result.append(group)
        return '-'.join(result)
