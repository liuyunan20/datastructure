from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = []
        i = 0
        n = len(intervals)
        while i < n:
            new_room = True
            for j in range(len(rooms)):
                if intervals[i][0] >= rooms[j][-1][1]:
                    rooms[j].append(intervals[i])
                    new_room = False
                    break
            if new_room:
                rooms.append([intervals[i]])
            i += 1
        return len(rooms)
