class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            return nums2[n // 2] if n % 2 == 1 else (nums2[(n // 2) - 1] + nums2[n // 2]) / 2
        if n == 0:
            return nums1[m // 2] if m % 2 == 1 else (nums1[(m // 2) - 1] + nums1[m // 2]) / 2
        current = 0
        if nums1[0] >= nums2[0]:
            array_base = nums2
            array_target = nums1
        else:
            array_base = nums1
            array_target = nums2

        for i in range(len(array_target)):
            target = array_target[i]
            start = current
            end = len(array_base)
            while start <= end:
                j = (start + end) // 2
                mid = array_base[j]
                if target == mid:
                    current = j + 1
                    array_base.insert(current, target)
                    break
                if target < mid:
                    end = j
                if target > mid:
                    start = j
                if start + 1 == end:
                    current = start + 1
                    array_base.insert(current, target)
                    break
            if current >= (m + n) // 2 or i == len(array_target) - 1:
                if (m + n) % 2 == 1:
                    warn = (m + n) // 2
                    return array_base[(m + n) // 2]
                else:
                    return (array_base[(m + n) // 2 - 1] + array_base[(m + n) // 2]) / 2
