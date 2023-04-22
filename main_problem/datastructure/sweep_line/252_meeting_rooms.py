class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        start = 0
        for interval in intervals:
            if interval[0] < start:
                return False
            start = interval[1]
        return True
