from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        for num in nums:
            freq.setdefault(num, 0)
            freq[num] += 1
        for num in freq:
            if len(result) < k:
                result.append(num)
            else:
                min_num = result[0]
                for n in result:
                    if freq[n] < freq[min_num]:
                        min_num = n
                if freq[num] > freq[min_num]:
                    result.remove(min_num)
                    result.append(num)
        return result
