class Solution:

    def __init__(self, w: List[int]):
        self.w = w

    def pickIndex(self) -> int:
        if len(self.w) == 1:
            return 0
        w_sum = sum(self.w)
        return random.choices([i for i in range(len(self.w))], weights=self.w, k=1)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
