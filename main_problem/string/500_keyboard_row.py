class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def in_one_row(w, r):
            for i in range(len(w)):
                if w[i] not in r:
                    return False
            return True
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []
        for word in words:
            word1 = word.lower()
            for row in rows:
                if word1[0] in row and in_one_row(word1, row):
                    result.append(word)
                    continue
        return result
