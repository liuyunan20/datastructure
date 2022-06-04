import math
from typing import List


class Solution:
    def calculateMaxInfoGain(self, petal_length: List[float], species: List[str]) -> float:
        def calculateEntropy(input_list: List[float]) -> float:
            freq = {}
            for x in input_list:
                freq.setdefault(x, 0)
                freq[x] += 1
            entropy = 0
            for x in freq:
                entropy += round(-freq[x] / len(input_list) * math.log(freq[x] / len(input_list), 2), 9)
            return entropy

        if not petal_length:
            return 0
        pl_sp = []
        for pl, sp in zip(petal_length, species):
            pl_sp.append((pl, sp))
        pl_sp.sort(key=lambda x:x[0])
        gain = 0
        for i in range(len(pl_sp)-1):
            l1 = [ps[1] for ps in pl_sp[:i+1]]
            l2 = [ps[1] for ps in pl_sp[i+1:]]
            gain = max(gain, calculateEntropy(species) - calculateEntropy(l1) * len(l1) / len(petal_length) - calculateEntropy(l2) * len(l2) / len(petal_length))
        return gain


pl1 = [1,2,3,4,5,6,7,8,9,10]
name = ["versicolor","versicolor","setosa","virginica","virginica","versicolor","versicolor","setosa","versicolor","versicolor"]
solution = Solution()
print(solution.calculateMaxInfoGain(pl1, name))
