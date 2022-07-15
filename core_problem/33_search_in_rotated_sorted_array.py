from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r, offset = 0, len(nums) - 1, 0
        if nums[l] > nums[r]:
            while l <= r:
                m = (l + r) // 2
                if nums[l] == nums[m]:
                    if target >= nums[0]:
                        offset = l - len(nums) + 1
                    else:
                        offset = l + 1
                    nums = nums[l+1:] + nums[:l+1]
                    break
                elif nums[l] < nums[m]:
                    l = m
                else:
                    r = m

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m + offset
            if target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return - 1
