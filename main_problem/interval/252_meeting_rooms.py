class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key= lambda x: x[0])
        n = len(intervals)
        i = 0
        while i + 1 < n:
            if intervals[i][1] > intervals[i + 1][0]:
                return False
            i += 1
        return True
