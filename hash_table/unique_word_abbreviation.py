from typing import List


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dictionary = {}
        for word in dictionary:
            abbr = word[0] + str(len(word) - 2) + word[-1]
            self.dictionary.setdefault(abbr, set())
            self.dictionary[abbr].add(word)

    def isUnique(self, word: str) -> bool:
        abbr = word[0] + str(len(word) - 2) + word[-1]
        if self.dictionary.get(abbr) and (len(self.dictionary[abbr]) != 1 or word not in self.dictionary[abbr]):
            return False
        return True


# Your ValidWordAbbr object will be instantiated and called as such:
obj = ValidWordAbbr(["a","a"])
param_1 = obj.isUnique("a")
print(param_1)
