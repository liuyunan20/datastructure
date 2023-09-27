class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        freq = {}
        nums.sort()
        for i, num in enumerate(nums):
            freq.setdefault(num, []).append(i)
        n = len(nums)
        result = set()
        for i in range(n - 2):
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 1):
                target = -nums[i] - nums[j]
                if target in freq:
                    for k in freq[target]:
                        if k > j:
                            result.add((nums[i], nums[j], nums[k]))
                            break
        return result
