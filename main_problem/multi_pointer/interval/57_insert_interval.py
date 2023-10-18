from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        start, end = newInterval
        if end < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        if start > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        n = len(intervals)
        result = []
        intervals[0][0] = min(start, intervals[0][0])
        for i in range(n):
            if end < intervals[i][0] and start != -1:
                result.append([start, end])
                start = -1
            elif intervals[i][0] <= start and end <= intervals[i][1]:
                result.append(intervals[i])
                start = -1
            elif intervals[i][0] <= start <= intervals[i][1]:
                start = intervals[i][0]
            elif intervals[i][0] <= end <= intervals[i][1]:
                end = intervals[i][1]
                result.append([start, end])
                start = -1
            if start > intervals[i][1] or end < intervals[i][0]:
                result.append(intervals[i])
        # result.sort(key=lambda x:x[0])
        if end > intervals[n - 1][1]:
            result.append([start, end])
        return result
