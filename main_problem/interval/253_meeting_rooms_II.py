from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        i = 0
        rooms = []
        while i < n:
            if not rooms:
                rooms.append(intervals[i])
            else:
                new_room = True
                for meet in rooms:
                    if meet[1] <= intervals[i][0]:
                        meet[1] = intervals[i][1]
                        new_room = False
                        break
                if new_room:
                    rooms.append(intervals[i])
            i += 1
        return len(rooms)
