class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n = len(word)
        if n == 1:
            return True
        first_capital = word[0].isupper()
        all_capital = word[1].isupper() and first_capital
        for i in range(1, n):
            if (all_capital and word[i].islower()) or (not all_capital and word[i].isupper()):
                return False
        return True
