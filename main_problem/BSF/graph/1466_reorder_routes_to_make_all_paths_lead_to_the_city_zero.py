class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        cities = {}
        for road in connections:
            cities.setdefault(road[0], []).append(road)
            cities.setdefault(road[1], []).append(road)
        queue = [0]
        result = 0
        visited = set()
        while queue:
            l = len(queue)
            for _ in range(l):
                city = queue.pop(0)
                visited.add(city)
                for road in cities[city]:
                    if city == road[0] and road[1] not in visited:
                        result += 1
                        queue.append(road[1])
                    elif road[0] not in visited:
                        queue.append(road[0])
        return result
