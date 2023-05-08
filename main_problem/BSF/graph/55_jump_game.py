from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        queue = [0]
        visited = set()
        while queue:
            l = len(queue)
            for _ in range(l):
                i = queue.pop(0)
                for s in range(1, nums[i] + 1):
                    if i + s not in visited:
                        if i + s >= n - 1:
                            return True
                        visited.add(i + s)
                        queue.append(i + s)
        return False
