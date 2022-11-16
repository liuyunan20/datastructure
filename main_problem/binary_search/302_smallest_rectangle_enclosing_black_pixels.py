class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m = len(image)
        n = len(image[0])

        start = 0
        end = y
        while start < end:
            j = (start + end) // 2
            no_one = True
            for i in range(m):
                mid = image[i][j]
                if mid == "1":
                    end = j
                    no_one = False
            if no_one:
                start = j + 1
        left = start
        print(left)
        start = y
        end = n - 1
        while start <= end:
            j = (start + end) // 2
            no_one = True
            for i in range(m):
                mid = image[i][j]
                if mid == "1":
                    start = j + 1
                    no_one = False
            if no_one:
                end = j - 1
        right = end

        start = 0
        end = x
        while start < end:
            i = (start + end) // 2
            no_one = True
            for j in range(n):
                mid = image[i][j]
                if mid == "1":
                    end = i
                    no_one = False
            if no_one:
                start = i + 1
        top = start
        start = x
        end = m - 1
        while start <= end:
            i = (start + end) // 2
            no_one = True
            for j in range(n):
                mid = image[i][j]
                if mid == "1":
                    start = i + 1
                    no_one = False
            if no_one:
                end = i - 1
        bottom = end
        print(left, right, top, bottom)
        return (bottom - top + 1) * (right - left + 1)
