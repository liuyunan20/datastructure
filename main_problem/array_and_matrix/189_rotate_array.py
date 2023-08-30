class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - k
        nums1 = []
        while i < n:
            nums.insert(0, nums.pop())
            i += 1
