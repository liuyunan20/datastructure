from typing import List

from sortedcontainers import SortedList


class SummaryRanges:

    def __init__(self):
        self.nums = SortedList()

    def addNum(self, value: int) -> None:
        if value not in self.nums:
            self.nums.add(value)

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        start = end = self.nums[0]
        n = len(self.nums)
        # if n == 1:
        #     return [[start, end]]
        i = 0
        while i < n:
            start = end = self.nums[i]
            while i + 1 < n and self.nums[i] + 1 == self.nums[i + 1]:
                i += 1
            end = self.nums[i]
            intervals.append([start, end])
            i += 1
        return intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
