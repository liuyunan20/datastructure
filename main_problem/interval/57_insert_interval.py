from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        i = 0
        a, b = newInterval
        result = []
        start = min(a, intervals[0][0])
        end = max(b, intervals[0][1])
        while i < n:
            start_i = intervals[i][0]
            end_i = intervals[i][1]
            if end < start_i:
                result.append([start, end])
                start = start_i
                end = end_i
            if start > end_i:
                result.append(intervals[i])
                i += 1
                continue
            else: # a <= end_i
                if start >= start_i:
                    start = start_i
                if end <= end_i:
                    end = end_i
                    # start = intervals[i + 1][0]
        #         else: # b > end_i
        #             if b < intervals[i + 1][0]:
        #                 result.append([start, b])
        #                 start = intervals[i + 1][0]
            i += 1
        # if a > intervals[i][1]:
        #     if n == 1:
        #         result.append(intervals[i])
        #     result.append([a, b])
        # else: # a < intervals[i][1]
        #     if b < intervals[i][0]:
        #         if n == 1:
        #             result.append([a, b])
        #             start = intervals[i][0]
        #     end = max(b, intervals[i][1])
        #     result.append([start, end])
        return result

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        start, end = newInterval
        result = []
        while i < n and start > intervals[i][0]:
            result.append(intervals[i])
            i += 1
        if not result or start > result[-1][1]:
            result.append(newInterval)
        else:
            result[-1][1] = max(end, result[-1][1])
        while i < n:
            if result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            else:
                result[-1][1] = max(intervals[i][1], result[-1][1])
            i += 1

        return result
