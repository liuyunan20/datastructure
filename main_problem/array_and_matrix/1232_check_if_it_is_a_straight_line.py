from _ast import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if (coordinates[1][1] - coordinates[0][1]) == 0:
            y = 0
        else:
            y = 1
            x = (coordinates[1][0] - coordinates[0][0]) / (coordinates[1][1] - coordinates[0][1])
        for i in range(1, n):
            if y == 0 and (coordinates[i][1] - coordinates[i-1][1]) != 0:
                return False
            if y != 0 and (coordinates[i][1] - coordinates[i-1][1] == 0 or (coordinates[i][0] - coordinates[i-1][0]) / (coordinates[i][1] - coordinates[i-1][1])) != x:
                return False
        return True
