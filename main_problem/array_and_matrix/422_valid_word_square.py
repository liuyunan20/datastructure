class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        def get_col(i):
            col = ""
            for word in words:
                col += word[i] if i < len(word) else ""
            return col

        for x in range(len(words)):
            if words[x] != get_col(x):
                return False
        return True
