class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_order = {}
        letters = "abcdefghijklmnopqrstuvwxyz"
        i = 0
        for letter in order:
            letter_order[letter] = letters[i]
            i += 1
        new_words = []
        for word in words:
            new_word = ""
            for letter in word:
                new_word += letter_order[letter]
            new_words.append(new_word)
        return True if new_words == sorted(new_words) else False
