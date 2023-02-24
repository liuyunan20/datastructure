from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)

        def palindrome(co):
            for string in co:
                if string != string[::-1]:
                    return False
            result.append(list(co))
            return True

        def dfs(idx, comb):
            if idx == n:
                palindrome(comb)
                return
            for i in range(idx, n):
                comb.append(s[idx: i + 1])
                dfs(i + 1, comb)
                comb.pop()
        dfs(0, [])
        return result
