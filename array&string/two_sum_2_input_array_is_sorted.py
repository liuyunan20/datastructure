from typing import List


class Solution:
    # use index method, slow
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            try:
                x = target - numbers[i]
                index = numbers.index(x, i + 1)
                return [i + 1, index + 1]
            except ValueError:
                continue

    # use dictionary, faster
    def twoSum_2(self, numbers: List[int], target: int) -> List[int]:
        index_nums = {}
        for i in range(len(numbers)):
            index_nums[numbers[i]] = i + 1
        for i in range(len(numbers)):
            if index_nums.get(target - numbers[i]):
                return [i + 1, index_nums[target - numbers[i]]]
