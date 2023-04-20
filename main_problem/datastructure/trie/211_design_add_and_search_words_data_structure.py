class WordDictionary:

    def __init__(self):
        self.dict = {}

    def addWord(self, word: str) -> None:
        self.dict.setdefault(len(word), []).append(word)

    def search(self, word: str) -> bool:
        n = len(word)
        if not self.dict.get(n):
            return False
        if "." not in word:
            return word in self.dict[n]
        for w in self.dict[n]:
            match = True
            for i in range(n):
                if word[i] != "." and word[i] != w[i]:
                    match = False
            if match:
                return True
        return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
