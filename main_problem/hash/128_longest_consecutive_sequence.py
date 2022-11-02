class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0
        for num in nums:
            if num - 1 not in nums:
                current_num = num
                current_length = 1
                while current_num + 1 in nums:
                    current_length += 1
                    current_num += 1
                result = max(result, current_length)
        return result
