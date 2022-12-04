from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n1 = len(firstList)
        n2 = len(secondList)
        i = j = 0
        result = []
        while i < n1 and j < n2:
            if secondList[j][0] <= firstList[i][0] <= secondList[j][1]:
                if secondList[j][0] <= firstList[i][1] <= secondList[j][1]:
                    result.append(firstList[i])
                    i += 1
                else:
                    result.append([firstList[i][0], secondList[j][1]])
                    j += 1
                continue
            if secondList[j][0] <= firstList[i][1] <= secondList[j][1]:
                if secondList[j][0] > firstList[i][0]:
                    result.append([secondList[j][0], firstList[i][1]])
                    i += 1
                continue
            if firstList[i][0] <= secondList[j][0] <= secondList[j][1] <= firstList[i][1]:
                result.append(secondList[j])
                j += 1
                continue
            if secondList[j][1] < firstList[i][0]:
                j += 1
                continue
            if firstList[i][1] < secondList[j][0]:
                i += 1
                continue
        return result
