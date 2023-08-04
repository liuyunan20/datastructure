class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        nums = {}
        for i, num in enumerate(arr):
            nums.setdefault(num, []).append(i)
        sub_lengths = {}

        def sub_length(i, length):
            num = arr[i]
            target = num + difference
            if target not in nums or i >= nums[target][-1]:
                sub_lengths[i] = length
                return length
            result = length
            for j in nums[target]:
                if j > i:
                    sub_lengths[j] = sub_length(j, length + 1)
                    result = max(result, sub_lengths[j])
            sub_lengths[i] = result
            return result

        res = 1
        for x in range(len(arr)):
            if x not in sub_lengths:
                res = max(sub_length(x, 1), res)
        return res
