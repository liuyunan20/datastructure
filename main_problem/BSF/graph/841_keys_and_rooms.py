from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = [0]
        visited = {0, }
        while queue:
            room = queue.pop(0)
            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)
                    visited.add(key)
        if len(visited) == len(rooms):
            return True
        return False
