class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        n = len(nums)
        result = []
        start = 0
        for i in range(n - 1):
            if nums[i] + 1 != nums[i + 1]:
                if start == i:
                    result.append(str(nums[i]))
                else:
                    result.append(str(nums[start]) + "->" + str(nums[i]))
                start = i + 1
        if start == n - 1:
            result.append(str(nums[start]))
        else:
            result.append(str(nums[start]) + "->" + str(nums[n - 1]))
        return result
