from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sums = {-1: 0}
        self.length = len(nums)
        sub = 0
        for i in range(len(self.nums)):
            self.sums[i] = sub + self.nums[i]
            sub = self.sums[i]

    def update_tle(self, index: int, val: int) -> None:
        d = val - self.nums[index]
        self.nums[index] = val
        for i in range(index, self.length):
            self.sums[i] += d

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] - self.sums[left - 1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
