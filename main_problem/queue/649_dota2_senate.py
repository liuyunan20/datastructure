class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = list(senate)
        i = 0
        ban = {'D': 'R', 'R': 'D'}
        win = {'D': 'Dire', 'R': 'Radiant'}
        while True:
            senator = queue.pop(0)
            queue.append(senator)
            i = 0
            n = len(queue)
            while i < n and queue[i] == senator:
                i += 1
            if i == n:
                return win[queue[0]]
            queue.pop(i)
