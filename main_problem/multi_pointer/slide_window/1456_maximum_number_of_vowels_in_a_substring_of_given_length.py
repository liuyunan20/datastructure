class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        i = 0
        counter = 0
        for l in s[i: k]:
            if l in vowel:
                counter += 1
        result = counter
        while i < n - k:
            if s[i] in vowel:
                counter -= 1
            if s[i + k] in vowel:
                counter += 1
            result = max(result, counter)
            i += 1
        return result
