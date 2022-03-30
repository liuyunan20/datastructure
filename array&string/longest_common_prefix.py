from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = len(min(strs))
        for i in range(1, min_length + 1):
            common = strs[0][0: i]
            for word in strs:
                if word[0: i] != common:
                    return word[0: i - 1]
        return strs[0][0: min_length]
