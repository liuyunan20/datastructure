class Solution:
    def longestPalindrome_tle(self, s: str) -> str:
            result = s[0]
            length = 0
            for i in range(len(s) - 1):
                for j in range(i, len(s)):
                    sub = s[i:j + 1]
                    if sub == sub[::-1] and len(sub) > length:
                            length = len(sub)
                            result = sub
            return result

    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        # check at every position if it's a center of a palindrome string, find the longest one
        for i in range(len(s) - 1):
            # check if the ith symbol or the space after the ith symbol is a center
            for a, b in [(i, i+1), (i-1, i+1)]:
                while a >= 0 and b < len(s) and s[a] == s[b]:
                    length = b - a + 1
                    # update result if the length of current palindrome substring is greater than result
                    if length > len(result):
                        result = s[a: b+1]
                    # expand palindrome substring
                    a -= 1
                    b += 1
        return result
