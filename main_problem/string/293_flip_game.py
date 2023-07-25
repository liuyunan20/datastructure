from typing import List


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        n = len(currentState)
        i = 0
        result = []
        while i < n - 1:
            if currentState[i] == currentState[i + 1] == "+":
                next_state = currentState[:i] + "--" + currentState[i + 2:]
                result.append(next_state)
            i += 1
        return result
