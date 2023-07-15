class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set()
        keys = keys.union(set(rooms[0]))
        rooms[0] = -1
        while keys:
            i = keys.pop()
            if rooms[i] != -1:
                keys = keys.union(set(rooms[i]))
                rooms[i] = -1
        for room in rooms:
            if room != -1:
                return False
        return True
