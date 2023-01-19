import string
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = [beginWord]
        step = 1
        word_length = len(beginWord)
        while queue:
            step += 1
            l = len(queue)
            for _ in range(l):
                cur_word = queue.pop(0)
                for i in range(word_length):
                    for letter in string.ascii_lowercase:
                        next_word = cur_word[:i] + letter + cur_word[i + 1:]
                        if next_word in wordList:
                            if next_word == endWord:
                                return step
                            queue.append(next_word)
                            wordList.discard(next_word)
        return 0
