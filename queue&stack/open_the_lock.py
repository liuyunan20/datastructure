from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        step = 0
        queue = ['0000']
        visited = set('0000',)
        if target == '0000':
            return 0
        if '0000' in deadends:
            return -1
        while queue:
            step += 1
            next_step = []
            for lock in queue:
                for i in range(4):
                    lock_colon = [x for x in lock]
                    x = lock_colon[i]
                    for d in (-1, 1):
                        lock_colon[i] = str((10 + int(x) + d) % 10)
                        lock_now = "".join(lock_colon)
                        if lock_now == target:
                            return step
                        if lock_now in deadends or lock_now in visited:
                            continue
                        visited.add(lock_now)
                        next_step.append(lock_now)
            queue = next_step
        return -1
