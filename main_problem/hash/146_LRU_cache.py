class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.age= []
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        if key in self.age:
            self.age.remove(key)
        self.age.append(key)
        if len(self.age) > self.capacity:
            self.age.pop(0)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        if key in self.age:
            self.age.remove(key)
        self.age.append(key)
        if len(self.age) > self.capacity:
            pop = self.age.pop(0)
            if len(self.cache) > self.capacity:
                self.cache.pop(pop)
