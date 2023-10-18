from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        start, end = newInterval
        n = len(intervals)
        result = []
        for i in range(n):
            if start > intervals[i][1] or end < intervals[i][0]:
                result.append(intervals[i])
            if end < intervals[i][0] and start <= newInterval[0]:
                result.append([start, end])
                start = end
            elif intervals[i][0] <= start and end <= intervals[i][1]:
                result.append(intervals[i])
                start = end
            elif intervals[i][0] <= start <= intervals[i][1]:
                start = intervals[i][0]
            elif intervals[i][0] <= end <= intervals[i][1]:
                end = intervals[i][1]
                result.append([start, end])
                start = end
            else:
                result.append(intervals[i])
        return result
