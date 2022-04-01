from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        start = [1, 1]
        while rowIndex - 1:
            for i in range(len(start) - 1):
                start[i] += start[i + 1]
            start.insert(0, 1)
            rowIndex -= 1
        return start
