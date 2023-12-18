class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        total = 0
        self.probability = []
        self.index = []
        for ai, bi, xi, yi in self.rects:
            area = (xi - ai + 1) * (yi - bi + 1)
            self.probability.append(area)
            total += area
        for i in range(len(self.probability)):
            self.index.append(i)
            self.probability[i] /= total

    def pick(self) -> List[int]:
        i = random.choices(self.index, weights=self.probability, k=1)
        ai, bi, xi, yi = self.rects[i[0]]
        u = random.randint(ai, xi)
        v = random.randint(bi, yi)
        return [u, v]
# param_1 = obj.pick()
