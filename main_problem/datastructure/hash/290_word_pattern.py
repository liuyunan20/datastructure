class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        letter_word = {}
        word_letter = {}
        i = 0
        while i < len(pattern):
            if not letter_word.get(pattern[i]) and not word_letter.get(s[i]):
                letter_word[pattern[i]] = s[i]
                word_letter[s[i]] = pattern[i]
            elif not letter_word.get(pattern[i]) or not word_letter.get(s[i]):
                return False
            elif letter_word[pattern[i]] != s[i] or word_letter[s[i]] != pattern[i]:
                return False
            i += 1
        return True
