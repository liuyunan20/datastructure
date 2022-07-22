from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def count_of_airplanes_tle(self, airplanes: List[Interval]) -> int:
        # write your code here
        if not airplanes:
            return 0
        time_plane = {}
        for i in airplanes:
            for hour in range(i.start, i.end):
                time_plane.setdefault(hour, 0)
                time_plane[hour] += 1
        return max(time_plane.values())

    def count_of_airplanes(self, airplanes: List[Interval]) -> int:
        # scan lines
        if not airplanes:
            return 0
        time_plane = []
        for i in airplanes:
            time_plane.append((i.start, 1))
            time_plane.append((i.end, -1))
        time_plane.sort()
        plane = 0
        result = 0
        for time, p in time_plane:
            plane += p
            result = max(plane, result)
        return result
