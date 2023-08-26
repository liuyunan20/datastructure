class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        k = 0
        while i <= j:
            if nums[i] == val:
                if nums[j] != val:
                    nums[i] = nums[j]
                    i += 1
                    j -= 1
                    k += 1
                else:
                    nums[j] = -1
                    j -= 1
                    k += 1
            else:
                i += 1
        return len(nums) - k
