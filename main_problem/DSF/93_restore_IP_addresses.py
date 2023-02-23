from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        result = []

        def valid_addr(positions):
            ip = ""
            for i, p in enumerate(positions):
                if i == 0:
                    num = s[:p + 1]
                else:
                    num = s[positions[i - 1] + 1: p + 1]
                ip += num + "."
                if (num.startswith("0") and len(num) > 1) or (num and int(num) > 255):
                    return False
            result.append(ip.rstrip("."))
            return True

        def dfs(comb, idx):
            if idx == n:
                return
            if len(comb) == 3:
                comb.append(n - 1)
                valid_addr(comb)
                comb.pop()
                return
            for i in range(idx, n - 1):
                comb.append(i)
                dfs(comb, i + 1)
                comb.pop()
        dfs([], 0)
        return result
