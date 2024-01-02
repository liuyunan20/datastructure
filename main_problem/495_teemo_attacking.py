class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        now = 0
        n = len(timeSeries)
        for i in range(n - 1):
            if timeSeries[i] + duration <= timeSeries[i + 1]:
                result += duration
            else:
                result += timeSeries[i + 1] - timeSeries[i]
        return result + duration
