class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq.setdefault(num, 0)
            freq[num] += 1
        freq_x = sorted(freq.items(), key=lambda x: -x[1])
        return freq_x[0][0]
