class TwoSum:

    def __init__(self):
        self.nums = []

    def add(self, number: int) -> None:
        self.nums.append(number)

    def find_tle(self, value: int) -> bool:
        for num in self.nums:
            if (value != 2 * num and value - num in set(self.nums)) or (value == 2 * num and self.nums.count(num) > 1):
                return True
        return False

    def find(self, value: int) -> bool:
        num_freq = {}
        for num in self.nums:
            num_freq.setdefault(num, 0)
            num_freq[num] += 1
        for num in num_freq:
            if (value != 2 * num and num_freq.get(value - num)) or (value == 2 * num and num_freq[value - num] > 1):
                return True
        return False
