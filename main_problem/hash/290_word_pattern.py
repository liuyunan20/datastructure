class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        pattern = list(pattern)
        pattern_word = {}
        visited = set()
        if len(pattern) != len(s):
            return False
        for letter, word in zip(pattern, s):
            if (not pattern_word.get(letter) and word in visited) or (pattern_word.get(letter) and pattern_word[letter] != word):
                return False
            else:
                pattern_word[letter] = word
            visited.add(word)
        return True
