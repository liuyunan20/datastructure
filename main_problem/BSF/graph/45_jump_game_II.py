from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        queue = [0]
        visited = set()
        step = 0
        while queue:
            step += 1
            l = len(queue)
            for _ in range(l):
                i = queue.pop(0)
                visited.add(i)
                for j in range(nums[i] + 1):
                    d = i + j
                    if d >= n - 1:
                        return step
                    if d not in visited:
                        queue.append(d)
