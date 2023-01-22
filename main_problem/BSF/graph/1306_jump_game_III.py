from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = {start,}
        queue = [start]
        while queue:
            i = queue.pop(0)
            for idx in [i + arr[i], i - arr[i]]:
                if 0 <= idx < n:
                    if arr[idx] == 0:
                        return True
                    if idx not in visited:
                        queue.append(idx)
                        visited.add(idx)
        return False
