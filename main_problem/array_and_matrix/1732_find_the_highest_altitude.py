class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for g in gain:
            alt = g + altitudes[-1]
            altitudes.append(alt)
        return max(altitudes)
