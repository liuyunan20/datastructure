from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            group.setdefault(''.join(sorted(list(word))), []).append(word)
        return group.values()
