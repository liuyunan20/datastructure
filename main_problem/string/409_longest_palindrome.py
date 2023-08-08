class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_letters = {}
        for i in range(len(s)):
            s_letters.setdefault(s[i], 0)
            s_letters[s[i]] += 1
        extra = 0
        result = 0
        for letter in s_letters:
            if s_letters[letter] % 2 == 1:
                extra = 1
            result += s_letters[letter] // 2
        return result * 2 + extra
