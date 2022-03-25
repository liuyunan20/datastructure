from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = []
        unlock_rooms = {0, }
        for key in rooms[0]:
            keys.append(key)
        while keys:
            i = keys.pop(0)
            unlock_rooms.add(i)
            if rooms[i]:
                for key in rooms[i]:
                    keys.append(key)
            rooms[i] = None
        if len(unlock_rooms) == len(rooms):
            return True
        return False
