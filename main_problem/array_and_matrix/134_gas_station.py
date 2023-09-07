from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def circle(idx):
            tank = 0
            start = idx - 1 if idx > 0 else len(gas) - 1
            while idx != start:
                tank += gas[idx] - cost[idx]
                if tank < 0:
                    return False
                else:
                    idx = 0 if idx == len(gas) - 1 else idx + 1
            return True

        if sum(gas) < sum(cost):
            return -1
        n = len(gas)
        i = 0
        for i in range(n):
            if circle(i):
                return i
        return -1
