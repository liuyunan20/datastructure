from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        i = 0
        j = 0
        result = 0
        peak = False
        while i < n:
            if i == n - 1 and peak:
                result = max(result, i - j + 1)
            elif i - 1 >= 0 and i + 1 < n:
                if arr[i - 1] >= arr[i] and arr[i] <= arr[i + 1]:
                    if peak:
                        result = max(result, i - j + 1)
                        peak = False
                    j = i
                if i - 1 >= 0 and arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                    peak = True
                if arr[i] == arr[i + 1]:
                    peak = False
                    j = i + 1
            i += 1
        return result
