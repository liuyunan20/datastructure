class Solution:
    def validPalindrome_tle(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        n = len(s)
        i = 0
        while i < n:
            new = s[:i] + s[i + 1:]
            if new == new[::-1]:
                return True
            i += 1
        return False

    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(p):
            i = 0
            j = len(p) - 1
            while i < j:
                if p[i] != p[j]:
                    return False
                i += 1
                j -= 1
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return check_palindrome(s[i + 1: j + 1]) or check_palindrome(s[i: j])
            i += 1
            j -= 1
        return True
