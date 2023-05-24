from typing import List


class Solution:
    def maxScore_tle(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def score(index):
            s = 0
            m = 100000
            for i in index:
                s += nums1[i]
                m = min(m, nums2[i])
            return s * m

        scores = []
        n = len(nums1)

        def dfs(i, index):
            if len(index) == k:
                scores.append(score(index))
                return
            else:
                for j in range(i, n):
                    index.append(j)
                    dfs(j + 1, list(index))
                    index.pop()

        dfs(0, [])
        return max(scores)
