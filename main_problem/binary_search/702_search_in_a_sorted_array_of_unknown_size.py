# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        start = 0
        end = 10000
        while start <= end:
            i = (start + end) // 2
            num = reader.get(i)
            if num == target:
                return i
            if num > target:
                end = i - 1
            elif num < target:
                start = i + 1
        return -1
