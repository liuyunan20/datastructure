from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''

        n1 = len(str1)
        n2 = len(str2)
        return str1[: gcd(n1, n2)]
