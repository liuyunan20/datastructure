from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = {0,}
        queue = [0]
        n = len(nums)
        while queue:
            l = len(queue)
            for _ in range(l):
                next_step = queue.pop()
                if nums[next_step] == n - 1:
                    return True
                for i in range(1, nums[next_step] + 1):
                    if next_step + i >= n - 1:
                        return True
                    if next_step + i not in visited:
                        queue.append(next_step + i)
                        visited.add(next_step + i)
        return False
