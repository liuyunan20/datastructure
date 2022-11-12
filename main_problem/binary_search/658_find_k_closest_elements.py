class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start = 0
        end = len(arr) - 1
        while start <= end:
            i = (start + end) // 2
            left = arr[start]
            mid = arr[i]
            right = arr[end]
            if abs(x - mid) == 0:
                break
            if abs(x - left) > abs(x - mid):
                start = i
            elif abs(x - left) < abs(x - mid):
                end = i
            else:
                if abs(x - left) > abs(x - right):
                    i = end
                break
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
