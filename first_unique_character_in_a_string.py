class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_list = list(s)
        freq_dict = {}
        for i, letter in enumerate(s_list):
            freq_dict.setdefault(letter, []).append(i)

        for letter in freq_dict:
            if len(freq_dict[letter]) == 1:
                return freq_dict[letter][0]
        return -1
