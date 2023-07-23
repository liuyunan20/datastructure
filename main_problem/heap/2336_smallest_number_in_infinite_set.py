import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.set = [1]
        self.num = 1
        heapq.heapify(self.set)

    def popSmallest(self) -> int:
        self.num += 1
        heapq.heappush(self.set, self.num)
        return heapq.heappop(self.set)

    def addBack(self, num: int) -> None:
        if num not in self.set and num < self.num:
            heapq.heappush(self.set, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
