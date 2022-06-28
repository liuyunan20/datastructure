from typing import List


class Solution:
    def threeSumClosest_tle(self, nums: List[int], target: int) -> int:
        num_dict = {}
        dif = 2147483647
        nums.sort()
        for i in range(len(nums)):
            j, m = i+1, len(nums)-1
            while j < m:
                if abs(dif) > abs(target - nums[i] - nums[j] - nums[m]):
                    dif = target - nums[i] - nums[j] - nums[m]
                if dif == 0:
                    return target
                if nums[i] + nums[j] + nums[m] < target:
                    j += 1
                else:
                    m -= 1
        return target - dif
