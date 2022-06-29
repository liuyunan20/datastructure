from typing import List
from sortedcontainers import SortedList


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

    def threeSumClosest_wrong(self, nums: List[int], target: int) -> int:
        num_dict = {}
        dif = 2147483647
        for num in nums:
            num_dict.setdefault(num, 0)
            num_dict[num] += 1
        nums = SortedList(num_dict.keys())
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                num = target-nums[i]-nums[j]
                if not num_dict.get(num):
                    index = nums.bisect_left(num)
                    if abs(dif) > abs(nums[index] - num):
                        dif = nums[index] - num
                    index = nums.bisect_right(num)
                    if abs(dif) > abs(nums[index] - num):
                        dif = nums[index] - num
                else:
                    if (num != nums[i] and num != nums[j]) or ((num == nums[i] and num_dict[nums[i]] > 1) or (num == nums[j] and num_dict[nums[j]] > 1)):
                        return target
        return target + dif
