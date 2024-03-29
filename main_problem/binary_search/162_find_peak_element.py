class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        i = 1
        while i < n - 1:
            if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
                return i
            i += 1


    def findPeakElement_binary_search(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        start = 0
        end = n - 1
        while start < end:
            i = (start + end) // 2
            if nums[i] < nums[i + 1]:
                start = i + 1
            if nums[i] > nums[i + 1]:
                end = i
        return start
