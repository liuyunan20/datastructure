class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = list(s)
        s_dict = {}
        for i, letter in enumerate(s_list):
            s_dict.setdefault(letter, []).append(i)
        t_list = list(t)
        t_dict = {}
        for i, letter in enumerate(t_list):
            t_dict.setdefault(letter, []).append(i)
        for (s_letter, s_position), (t_letter, t_position) in zip(s_dict.items(), t_dict.items()):
            if s_position != t_position:
                return False
        return True
