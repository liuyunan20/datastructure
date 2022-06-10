from bisect import bisect
from typing import List


class Solution:
    def platesBetweenCandles_tle(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []
        for i, item in enumerate(list(s)):
            if item == "|":
                candles.append(i)
        result = []
        for m, n in queries:
            for p, i in enumerate(candles):
                if i >= m:
                    start = i
                    start_p = p
                    break
            for p, i in enumerate(candles[::-1]):
                if i <= n:
                    end = i
                    end_p = len(candles) - 1 - p
                    break
            count = end - start - 1 - (end_p - start_p - 1)
            if count >= 0:
                result.append(count)
            else:
                result.append(0)
        return result


def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []
        for i, item in enumerate(list(s)):
            if item == "|":
                candles.append(i)
        result = []
        for m, n in queries:
            start = bisect.bisect_left(candles, m)
            if start == len(candles):
                result.append(0)
                continue
            end = bisect.bisect(candles, n) - 1
            if end <= 0:
                result.append(0)
                continue
            count = candles[end] - candles[start] - 1 - (end - start - 1)
            if count >= 0:
                result.append(count)
            else:
                result.append(0)
        return result
