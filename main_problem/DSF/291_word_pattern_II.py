class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        letter_word = {}
        word_letter = {}
        p = len(pattern)
        sl = len(s)

        def dfs(i, j):
            if i == p and j == sl:
                return True
            if i == p or j == sl:
                return False
            letter = pattern[i]
            for k in range(j, sl):
                word = s[j: k + 1]
                if word not in word_letter and letter not in letter_word:
                    word_letter[word] = letter
                    letter_word[letter] = word
                    if dfs(i + 1, k + 1):
                        return True
                    del word_letter[word]
                    del letter_word[letter]
                elif word in word_letter and letter in letter_word and word_letter[word] == letter and letter_word[
                    letter] == word:
                    if dfs(i + 1, k + 1):
                        return True
            return False

        return dfs(0, 0)
