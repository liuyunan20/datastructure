class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        digits = {'6': '9', '9': '6', '1': '1', '0': '0', '8': '8'}
        n = len(num)
        new = ''
        i = 0
        while i < n:
            if num[i] not in digits:
                return False
            new += digits[num[i]]
            i += 1
        if new[::-1] != num:
            return False
        return True
