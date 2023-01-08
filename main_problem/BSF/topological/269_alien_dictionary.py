from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        order_0 = []
        letters = set()
        for word in words:
            if word[0] not in order_0:
                order_0.append(word[0])
            letters.update(set(list(word)))
        pre_letters = {}
        for i in range(1, len(order_0)):
            pre_letters.setdefault(order_0[i], []).append(order_0[i - 1])
        for i in range(1, n):
            j = 0
            while words[i - 1][j] == words[i][j]:
                j += 1
                if j == len(words[i - 1]):
                    break
                if j == len(words[i]):
                    return ""
            if j < len(words[i - 1]):
                pre_letters.setdefault(words[i][j], []).append(words[i - 1][j])
        visited = set()
        finished = []
        def bfs(suf):
            if suf not in pre_letters:
                if suf not in finished:
                    finished.append(suf)
                return True
            if suf in finished:
                return True
            if suf in visited:
                return False
            visited.add(suf)
            for pre in pre_letters[suf]:
                if bfs(pre):
                    if pre not in finished:
                        finished.append(pre)
                else:
                    return False
            finished.append(suf)
            visited.discard(suf)
            return True
        for letter in letters:
            if not bfs(letter):
                return ""
        return ''.join(finished)
