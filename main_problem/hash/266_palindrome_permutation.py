class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        letters = {}
        for i in s:
            letters.setdefault(i, 0)
            letters[i] += 1
        counter = 0
        for i in letters:
            if letters[i] % 2 == 1:
                counter += 1
        return counter <= 1
