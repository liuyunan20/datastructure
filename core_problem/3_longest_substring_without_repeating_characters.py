class Solution:
    def lengthOfLongestSubstring_1(self, s: str) -> int:
        result = 0
        start = 0
        sub = {}
        for i in range(len(s)):
            if sub.get(s[i]) is not None and sub[s[i]] >= start:
                start = sub[s[i]] + 1
            sub[s[i]] = i
            result = max(result, i-start+1)
        return result

    def lengthOfLongestSubstring_2(self, s: str) -> int:
        if not s:
            return 0
        s_dict = {}
        i, j = -1, 0
        s = list(s)
        result = 0
        while j < len(s):
            if s_dict.get(s[j]) is not None:
                i = max(i, s_dict[s[j]])
            s_dict[s[j]] = j
            result = max(result, j - i)
            j += 1
        return result
