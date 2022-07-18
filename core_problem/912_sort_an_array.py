from typing import List


class Solution:
    def sortArray_tle(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if not result:
                result.append(num)
            elif num <= result[0]:
                result.insert(0, num)
            elif num >= result[-1]:
                result.append(num)
            else:
                for i in range(len(result)-1):
                    if result[i] < num <= result[i+1]:
                        result.insert(i+1, num)
                        break
        return result
