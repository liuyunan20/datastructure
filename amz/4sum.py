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

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        num_dict = {}
        for num in nums:
            num_dict.setdefault(num, 0)
            num_dict[num] += 1
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue
                    n = target - nums[i] - nums[j] - nums[k]
                    if n > nums[k] and num_dict.get(n) is not None:
                        result.append([nums[i], nums[j], nums[k], n])
                    if n == nums[k]:
                        s = int(n == nums[i]) + int(n == nums[j]) + int(n == nums[k])
                        if num_dict[n] > s:
                            result.append([nums[i], nums[j], nums[k], n])
        return result
