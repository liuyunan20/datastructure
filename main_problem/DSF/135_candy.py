class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        result = [1 for _ in range(n)]
        lowest = min(ratings)
        low_position = []
        visited = set()
        for i, r in enumerate(ratings):
            if r == lowest:
                low_position.append((i, r))

        while low_position:
            low_position.sort(key=lambda x: x[1])
            l = len(low_position)
            for _ in range(l):
                p, r = low_position.pop(0)
                visited.add(p)
                left = p - 1
                while left >= 0 and ratings[left] > ratings[left + 1]:
                    result[left] = max(result[left + 1] + 1, result[left])
                    left -= 1
                if left >= 0 and left not in visited:
                    low_position.append((left, ratings[left]))
                right = p + 1
                while right < n and ratings[right] > ratings[right - 1]:
                    result[right] = max(result[right - 1] + 1, result[right])
                    right += 1
                if right < n and right not in visited:
                    low_position.append((right, ratings[right]))

        return sum(result)
