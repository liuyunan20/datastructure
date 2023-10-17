class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        result = []
        start, end = intervals[0]
        for i in range(n - 1):
            end = max(intervals[i][1], end)
            if end < intervals[i + 1][0]:
                result.append([start, end])
                start = intervals[i + 1][0]
        result.append([start, max(end, intervals[n - 1][1])])
        return result
