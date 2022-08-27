from typing import List


class Solution:
    # wrong answer,
    # can't find the combination of multiple candidate1 and multiple candidate2 and so on
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        for cdd in candidates:
            i = 1
            combination = []
            if cdd == target:
                result.append([cdd])
            while target - cdd * i >= 0:
                if target - cdd * i in candidates:
                    combination = [cdd for _ in range(i)]
                    combination.append(target - cdd * i)
                    if len(combination) == 2 and cdd > target - cdd:
                        i += 1
                        continue
                    result.append(combination)
                i += 1

        return result
