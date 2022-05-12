from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        num_hashmap = {}
        result = 0
        for num1 in nums1:
            for num2 in nums2:
                num_hashmap.setdefault(num1 + num2, 0)
                num_hashmap[num1 + num2] += 1
        for num3 in nums3:
            for num4 in nums4:
                if num_hashmap.get(-num3 - num4):
                    result += num_hashmap[-num3 - num4]
        return result
