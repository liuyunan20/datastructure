class Solution:
    def subarraySum_tle(self, nums: List[int], k: int) -> int:
        # not use hash
        result = 0
        l = len(nums)
        for i in range(l):
            if nums[i] == k:
                result += 1
            j = 1
            current_sum = nums[i]
            while i + j < l:
                current_sum += nums[i + j]
                if current_sum == k:
                    result += 1
                j += 1
        return result

    def subarraySum_hashmap(self, nums: List[int], k: int) -> int:
        result = 0
        sub_sums = {0: 1}
        sub_sum = 0
        for num in nums:
            sub_sum += num
            if sub_sums.get(sub_sum - k):
                result += sub_sums[sub_sum - k]
            sub_sums.setdefault(sub_sum, 0)
            sub_sums[sub_sum] += 1
        return result
