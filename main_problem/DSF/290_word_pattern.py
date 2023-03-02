class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = s.split()
        if len(s) != len(pattern):
            return False
        letter_word = {}
        word_letter = {}
        for letter, word in zip(pattern, s):
            if letter_word.get(letter) is None:
                letter_word[letter] = word
            elif letter_word[letter] != word:
                return False
            if word_letter.get(word) is None:
                word_letter[word] = letter
            elif word_letter[word] != letter:
                return False
        return True
