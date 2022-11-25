class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = j = 0
        m = len(nums1)
        n = len(nums2)
        result = []
        while i < m and j < n:
            if nums1[i] == nums2[j] and nums1[i] not in result:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result

    def intersection_2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """jump over duplicates"""
        nums1.sort()
        nums2.sort()
        i = j = 0
        m = len(nums1)
        n = len(nums2)
        result = set()
        while i < m and j < n:
            if i + 1 < m and nums1[i] == nums1[i + 1]:
                i += 1
            if j + 1 < n and nums2[j] == nums2[j + 1]:
                j += 1
            if nums1[i] == nums2[j]:
                result.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result
