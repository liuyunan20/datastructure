from _ast import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        positions_0 = []
        result = []
        for i, num in enumerate(nums):
            if num == 0:
                positions_0.append(i)
            else:
                product *= num
        for num in nums:
            if not positions_0:
                result.append(product // num)
            else:
                if len(positions_0) == 1:
                    if num != 0:
                        result.append(0)
                    else:
                        result.append(product)
                else:
                    result.append(0)
        return result
