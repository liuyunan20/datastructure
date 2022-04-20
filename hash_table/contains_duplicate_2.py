from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_position = {}
        for i, num in enumerate(nums):
            num_position.setdefault(num, []).append(i)
        for num in num_position:
            if len(num_position[num]) > 1:
                for i in range(len(num_position[num]) - 1):
                    if num_position[num][i + 1] - num_position[num][i] <= k:
                        return True
        return False
