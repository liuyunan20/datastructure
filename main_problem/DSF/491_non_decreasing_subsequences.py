from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def dfs(subseq, idx):
            if idx == n + 1:
                return
            if len(subseq) > 1:
                if subseq not in result:
                    result.append(list(subseq))
            for i in range(idx, n):
                if not subseq or subseq[-1] <= nums[i]:
                    subseq.append(nums[i])
                    dfs(subseq, i + 1)
                    subseq.pop()
        dfs([], 0)
        return result
