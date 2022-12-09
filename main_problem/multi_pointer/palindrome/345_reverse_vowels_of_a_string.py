class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        positions = []
        vowel_s = ''
        for i, letter in enumerate(s):
            if letter in vowels:
                positions.append(i)
                vowel_s += letter
        vowel_s = vowel_s[::-1]
        print(vowel_s)
        s = list(s)
        print(s)
        for i in range(len(positions)):
            s[positions[i]] = vowel_s[i]
        return ''.join(s)
