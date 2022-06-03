import math


class Solution:
    def calculateEntropy(self, input: List[int]) -> float:
        freq = {}
        for x in input:
            freq.setdefault(x, 0)
            freq[x] += 1
        entropy = 0
        for x in freq:
            entropy += round(-freq[x] / len(input) * math.log(freq[x] / len(input), 2), 9)
        return entropy
