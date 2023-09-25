class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in freq:
                return [freq[diff][0] + 1, i + 1]
            freq.setdefault(num, []).append(i)
