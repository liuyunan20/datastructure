class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start = 0
        end = len(arr) - 1
        while start <= end:
            i = (start + end) // 2
            left = arr[start]
            mid = arr[i]
            right = arr[end]
            if mid == x:
                break
            if mid < x:
                start = i
            if mid > x:
                end = i
            if end == start:
                break
            if end == start + 1:
                if abs(x - arr[start]) > abs(x - arr[end]):
                    i = end
                else:
                    i = start
                break
        while i - 1 >= 0 and arr[i - 1] == arr[i]:
            i -= 1
        print(i)
        result = [arr[i]]
        f = -1
        b = 1
        while k > 1:
            if i + f >= 0 and i + b < len(arr):
                if abs(x - arr[i + f]) <= abs(x - arr[i + b]):
                    result.insert(0, arr[i + f])
                    f -= 1
                else:
                    result.append(arr[i + b])
                    b += 1
            elif i + f < 0 and i + b < len(arr):
                result.append(arr[i + b])
                b += 1
            elif i + f >= 0 and i + b >= len(arr):
                result.insert(0, arr[i + f])
                f -= 1
            k -= 1
        return result
