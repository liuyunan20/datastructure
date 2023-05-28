from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flower = 0
        l = len(flowerbed)
        if (l == 1 and flowerbed[0] == 0) or (l > 1 and flowerbed[0] == flowerbed[1] == 0):
            flower += 1
            flowerbed[0] = 1
        for i in range(1, l - 1):
            if i + 1 < l and flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                flower += 1
                flowerbed[i] = 1
        if l > 1 and flowerbed[l - 2] == flowerbed[l - 1] == 0:
            flower += 1
        if flower >= n:
            return True
        return False
