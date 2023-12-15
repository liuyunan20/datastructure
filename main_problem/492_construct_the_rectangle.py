class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = 1
        l = area
        result = [l, w]
        while w <= l:
            w += 1
            l = area /w
            if l == int(l) and w <= l:
                result = [int(l), w]
        return  result
