class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.used = []
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            if key in self.used:
                self.used.remove(key)
                self.used.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.cap and key not in self.cache:
            recent = self.used[0]
            del self.cache[recent]
            self.used.remove(recent)
        self.cache[key] = value
        if key in self.used:
            self.used.remove(key)
        self.used.append(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
