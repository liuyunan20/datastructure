class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # brute force
        positions = []
        for i, num in enumerate(nums):
            if num == target:
                positions.append(i)
        if not positions:
            return [-1, -1]
        return [positions[0], positions[-1]]
