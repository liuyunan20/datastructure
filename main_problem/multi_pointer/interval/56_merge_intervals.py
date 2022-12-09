class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        n = len(intervals)
        if n == 1:
            return intervals
        i = 1
        result = []
        start = intervals[0][0]
        end = intervals[0][1]
        while i < n:
            if end < intervals[i][0]:
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                if end < intervals[i][1]:
                    end = intervals[i][1]
            if i == n - 1:
                result.append([start, end])
            i += 1
        return result
