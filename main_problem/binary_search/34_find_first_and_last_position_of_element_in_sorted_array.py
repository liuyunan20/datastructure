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

    def searchRange_binary_search(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        if l == 0:
            return [-1, -1]
        found = False
        i = l // 2
        start = 0
        end = l - 1
        while start <= end:
            if nums[i] == target:
                found = True
                break
            elif nums[i] > target:
                end = i - 1
            elif nums[i] < target:
                start = i + 1
            i = (end - start) // 2 + start
        if not found:
            return [-1, -1]
        else:
            j = 0
            while i + j < l and nums[i + j] == target:
                j += 1
            last = i + j - 1
            j = 0
            while i - j >= 0 and nums[i - j] == target:
                j += 1
            first = i - j + 1
            return [first, last]
