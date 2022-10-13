class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        if "" in strs:
            return ""
        i = 0
        while True:
            if i >= len(strs[0]):
                return result
            letter = strs[0][i]
            for word in strs:
                if i >= len(word) or (i < len(word) and word[i] != letter):
                    return result
            result += letter
            i += 1
