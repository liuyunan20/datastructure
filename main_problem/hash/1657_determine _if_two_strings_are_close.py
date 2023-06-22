class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        freq1 = {}
        freq2 = {}
        for w1, w2 in zip(word1, word2):
            freq1.setdefault(w1, 0)
            freq1[w1] += 1
            freq2.setdefault(w2, 0)
            freq2[w2] += 1
        return freq1.keys() == freq2.keys() and sorted(freq1.values()) == sorted(freq2.values())
