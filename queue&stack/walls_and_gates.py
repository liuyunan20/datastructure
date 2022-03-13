class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])

        visited = []
        gates = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                     gates.append((i, j))
        for gate in gates:
            current_round = [gate]
            step = 0
            while current_round:
                step += 1
                next_round = []
                for position in current_round:
                    (i, j) = position
                    if i - 1 >= 0 and rooms[i - 1][j] > step:
                        rooms[i - 1][j] = step
                        next_round.append((i - 1, j))
                    if i + 1 < m and rooms[i + 1][j] > step:
                        rooms[i + 1][j] = step
                        next_round.append((i + 1, j))
                    if j - 1 >= 0 and rooms[i][j - 1] > step:
                        rooms[i][j - 1] = step
                        next_round.append((i, j - 1))
                    if j + 1 < n and rooms[i][j + 1] > step:
                        rooms[i][j + 1] = step
                        next_round.append((i, j + 1))
                current_round = next_round
