# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while start <= end:
            i = (end - start) // 2 + start
            if isBadVersion(i):
                end = i - 1
            else:
                start = i + 1
        return start
