class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2 = len(nums2)
        result = []
        for num in nums1:
            exist = False
            i = nums2.index(num)
            for j in range(i + 1, n2):
                if nums2[j] > num:
                    result.append(nums2[j])
                    exist = True
                    break
            if not exist:
                result.append(-1)
        return result
