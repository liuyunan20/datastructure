import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        for i in range(len(s)):
            if s[i] not in string.ascii_letters and s[i] not in string.digits:
                s[i] = ''
        s = ''.join(s).lower()
        if s == s[::-1]:
            return True
        return False
