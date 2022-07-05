from typing import List


class Solution:
    def fourSum_tle(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        nums.sort()
        s_dict = {}
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                s_dict.setdefault(nums[i]+nums[j], []).append([i, j])
        s_list = list(s_dict.keys())
        for s in s_list:
            num = target - s
            if num != s and s_dict.get(num) is not None:
                for i, j in s_dict[s]:
                    for m, n in s_dict[num]:
                        if i != m and i != n and j != m and j != n:
                            result.add(tuple(sorted([nums[i], nums[j], nums[m], nums[n]])))
            if num == s and len(s_dict[s]) > 1:
                for i, j in s_dict[s]:
                    for m, n in s_dict[num]:
                        if i != m and i != n and j != m and j != n:
                            result.add(tuple(sorted([nums[i], nums[j], nums[m], nums[n]])))
        return result
