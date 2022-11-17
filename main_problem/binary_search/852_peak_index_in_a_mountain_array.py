class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        start = 0
        end = n - 1
        while start <= end:
            i = (start + end) // 2
            if i - 1 >= 0 and i + 1 < n and arr[i - 1] < arr[i] and arr[i + 1] < arr[i]:
                return i
            if i - 1 >= 0 and arr[i - 1] > arr[i]:
                end = i - 1
            if i + 1 < n - 1 and arr[i + 1] > arr[i]:
                start = i + 1
