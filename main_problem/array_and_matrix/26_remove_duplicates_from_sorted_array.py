from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                nums[i] = 101
            else:
                visited.add(nums[i])
        nums.sort()
        return len(visited)
