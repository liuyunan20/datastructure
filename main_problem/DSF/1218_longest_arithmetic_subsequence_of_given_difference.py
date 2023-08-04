class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        nums = {}
        for i, num in enumerate(arr):
            nums.setdefault(num, []).append(i)
        sub_lengths = {}

        sub_lengths = {}
        def sub_length(i):
            num = arr[i]
            target = num + difference
            if target not in nums or i >= nums[target][-1]:
                sub_lengths[i] = 1
                return 1
            result = 1
            for j in nums[target]:
                if j > i:
                    if j not in sub_lengths:
                        sub_lengths[j] = sub_length(j)
                    result = max(result, sub_lengths[j])
            sub_lengths[i] = result + 1
            return sub_lengths[i]
        res = 1
        for x in range(len(arr)):
            if x not in sub_lengths:
                res = max(sub_length(x), res)
        return res

        res = 1
        for x in range(len(arr)):
            if x not in sub_lengths:
                res = max(sub_length(x, 1), res)
        return res
