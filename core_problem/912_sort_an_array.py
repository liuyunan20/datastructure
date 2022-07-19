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

    # quick sort, if nums is empty, return it
    # select a random value in the list, go through the list
    # put the same value to middle part, bigger value to right part, smaller value to left part
    # call the function itself with left and right part as argument
    # return left + mid + right
    def sortArray(self, nums: List[int]) -> List[int]:
        left = []
        mid = []
        right = []
        if not nums:
            return nums
        key_value = nums[len(nums)//2]
        for num in nums:
            if num == key_value:
                mid.append(num)
            if num > key_value:
                right.append(num)
            if num < key_value:
                left.append(num)
        return self.sortArray(left) + mid + self.sortArray(right)
