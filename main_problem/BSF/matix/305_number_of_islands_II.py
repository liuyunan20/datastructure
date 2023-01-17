from typing import List


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        cur_edges = []
        cur_num = []
        visited = set()
        num = 0
        for p in positions:
            if tuple(p) in visited:
                cur_num.append(len(cur_edges))
                continue
            visited.add(tuple(p))
            connect = 0
            fusion = []
            for i, edge in enumerate(cur_edges):
                if tuple(p) in edge:
                    connect += 1
                    fusion.append(i)
            edge = set()
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r = p[0] + d[0]
                c = p[1] + d[1]
                if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                    edge.add((r, c))
            if connect:
                cur_edges[fusion[0]].update(edge)
                for i in fusion[1:]:
                    cur_edges[fusion[0]].update(cur_edges[i])
                for i in fusion[1:]:
                    cur_edges[i] = []
            if not connect:
                cur_edges.append(edge)
            num -= connect - 1
            cur_num.append(num)
        return cur_num

    def numIslands2_bfs_tle(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        l = len(positions)
        answer = []
        for i in range(l):
            lands = positions[:i + 1]
            visited = set()
            counter = 0
            for p in lands:
                po = tuple(p)
                queue = []
                if po not in visited:
                    queue.append(po)
                    counter += 1
                visited.add(po)
                while queue:
                    pos = queue.pop(0)
                    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        r = pos[0] + d[0]
                        c = pos[1] + d[1]
                        if 0 <= r < m and 0 <= c < n and (r, c) not in visited and [r, c] in lands:
                            queue.append((r, c))
                            visited.add((r, c))
            answer.append(counter)
        return answer
