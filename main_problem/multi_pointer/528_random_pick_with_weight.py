import random
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.index = [i for i in range(len(w))]

    def pickIndex(self) -> int:
        if len(self.w) == 1:
            return 0
        return random.choices(self.index, weights=self.w, k=1)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
