from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        visited = {0, }
        queue = [0]
        step = 0
        while queue:
            step += 1
            l = len(queue)
            for _ in range(l):
                position = queue.pop(0)
                for i in range(1, nums[position] + 1):
                    next_p = position + i
                    if next_p >= n - 1:
                        return step
                    if next_p not in visited:
                        queue.append(next_p)
                        visited.add(next_p)
