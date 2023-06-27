class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        self.counter.append(t)
        n = len(self.counter)
        i = n - 1
        result = 0
        while i >= 0:
            if t - 3000 <= self.counter[i] <= t:
                result += 1
            i -= 1
        return result
