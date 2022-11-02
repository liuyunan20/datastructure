class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            key = "".join(sorted(list(word)))
            result.setdefault(key, []).append(word)
        return list(result.values())
