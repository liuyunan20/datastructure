from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for s in strs:
            anagram.setdefault("".join(sorted(s)), []).append(s)
        return anagram.values()
