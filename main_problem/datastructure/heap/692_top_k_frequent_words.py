from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            freq.setdefault(word, 0)
            freq[word] += 1
        freq = sorted(freq.items(), key=lambda x: -x[1])
        print(freq)
        n = len(freq)
        result = []
        words = [freq[0][0]]
        i = 0
        while i < n:
            if i + 1 < n and freq[i][1] != freq[i + 1][1]:
                result += sorted(words)
                words = [freq[i + 1][0]]
                i += 1
            elif i + 1 < n and freq[i][1] == freq[i + 1][1]:
                words.append(freq[i + 1][0])
                i += 1
                continue
            else:
                result += sorted(words)
                i += 1
        return result[:k]
