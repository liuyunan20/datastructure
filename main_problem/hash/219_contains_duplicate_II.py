class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}
        for i, num in enumerate(nums):
            if mapping.get(num) is None or i - mapping[num] > k:
                mapping[num] = i
            else:
                return True
        return False
