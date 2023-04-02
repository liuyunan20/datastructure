from _ast import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_order = {}
        num = 1
        for letter in order:
            letter_order[letter] = num
            num += 1
        i = 0
        l = 0
        next_round = False
        while True:
            prior = 0
            for word in words:
                l = max(l, len(word))
                cur = letter_order[word[i]]if i < len(word) else 0
                if cur < prior:
                    return False
                if cur == prior:
                    next_round = True
                prior = cur
            i += 1
            if not next_round:
                return True
            next_round = False
            if i == l:
                return True
