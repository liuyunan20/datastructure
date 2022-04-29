class Solution:
    def lengthOfLongestSubstring_tle(self, s: str) -> int:
        if not s:
            return 0
        length = len(s)
        result = []
        for i in range(length):
            for j in range(length, -1, -1):
                if len(s[i:j]) == len(set(s[i:j])):
                    result.append(len(s[i:j]))
                    continue
        return max(result)

    def lengthOfLongestSubstring_tle2(self, s: str) -> int:
        if not s:
            return 0
        length = len(s)
        if length == len(set(s)):
            return length
        result = 0
        for i in range(length):
            for j in range(length, i + result -1, -1):
                sub = s[i:j]
                if len(sub) == len(set(sub)):
                    result = max(len(sub), result)
                    continue
            if i + result == length:
                return result
        return result

    def lengthOfLongestSubstring_hashmap(self, s: str) -> int:
        if not s:
            return 0
        s_list = list(s)
        letter_position = {}
        result = 0
        sub_start = 0
        sub_result = 0
        for i, letter in enumerate(s_list):
            letter_position.setdefault(letter, [])
            letter_position[letter].append(i)
            if len(letter_position[letter]) > 1:
                sub_start = max(sub_start, letter_position[letter][-2] + 1)
                sub_result = i - sub_start + 1
            else:
                sub_result += 1
            result = max(result, sub_result)
        return result
