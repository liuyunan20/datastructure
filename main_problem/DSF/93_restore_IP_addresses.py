class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)

        def valid_addr(positions):
            for i, p in enumerate(positions):
                print(positions)
                if i == 0:
                    num = s[:p + 1]
                else:
                    num = s[positions[i - 1] + 1: p + 1]
                print(num)
                if (num.startswith("0") and len(num) > 1) or (num and int(num) > 255):
                    return False

            return True

        result = []

        def dfs(comb, idx):
            if idx == n:
                return
            if len(comb) == 3:
                comb.append(n - 1)
                if valid_addr(comb):
                    result.append(list(comb))
                comb.pop()
                return
            for i in range(idx, n - 1):
                comb.append(i)
                dfs(comb, i + 1)
                comb.pop()

        dfs([], 0)

        return result
