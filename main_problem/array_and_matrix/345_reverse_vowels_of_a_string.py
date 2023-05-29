class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        vowels = []
        s = list(s)
        for i in range(n):
            if s[i] in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                vowels.append(s[i])
                s[i] = 0
        for i in range(n):
            if s[i] == 0:
                s[i] = vowels.pop()
        return ''.join(s)
