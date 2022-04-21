from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for word in strs:
            words.setdefault(''.join(sorted(word)), []).append(word)
        return list(words.values())
