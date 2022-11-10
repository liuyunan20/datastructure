class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        result = nums[start]
        while start <= end:
            i = (start + end) // 2
            left = nums[start]
            mid = nums[i]
            right = nums[end]
            if left <= mid <= right:
                result = min(result, mid)
                start += 1
                end -= 1
                continue
            if left <= mid:
                start = i + 1
            if left > mid:
                end = i

        return result
