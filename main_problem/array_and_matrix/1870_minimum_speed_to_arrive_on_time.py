class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > hour + 1:
            return -1
        result = 1
        while True:
            time = 0
            for i in range(len(dist) - 1):
                time += dist[i] // result if dist[i] % result == 0 else dist[i] // result + 1
            time += dist[-1] / result
            if time <= hour:
                return result
            result += 1
