from typing import List


class Solution:
    def ladderLength_tle(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def check_neighbor(w1, w2):
            diff = 0
            for l1, l2 in zip(w1, w2):
                if l1 != l2:
                    diff += 1
            if diff == 1:
                return True
            return False

        word_neighbor = {beginWord: set()}
        for word in wordList:
            if check_neighbor(beginWord, word):
                word_neighbor[beginWord].add(word)
            word_neighbor[word] = set()
            for word2 in wordList:
                if check_neighbor(word, word2):
                    word_neighbor[word].add(word2)

        visited = set()
        queue = [beginWord]
        step = 1
        while queue:
            step += 1
            l = len(queue)
            for _ in range(l):
                cur_word = queue.pop(0)
                for next_word in word_neighbor[cur_word]:
                    if next_word == endWord:
                        return step
                    if next_word not in visited:
                        queue.append(next_word)
                        visited.add(next_word)
        return 0
