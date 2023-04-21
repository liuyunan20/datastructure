from typing import List


class StreamChecker:

    def __init__(self, words: List[str]):
        self.dict = {}
        for word in words:
            self.dict.setdefault(len(word), set()).add(word)
        self.stream = ""

    def query(self, letter: str) -> bool:
        self.stream += letter
        for n in self.dict:
            if n > len(self.stream):
                continue
            suffix = self.stream[len(self.stream) - n:]
            if suffix in self.dict[n]:
                return True
        return False




# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
