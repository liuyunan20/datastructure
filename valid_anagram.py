class Solution:
    # solution I thought
    def isAnagram_1(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        if len(s_list) == len(t_list):
            for letter in s_list:
                if letter not in t_list:
                    return False
                t_list.remove(letter)
            return True
        else:
            return False

    # solution suggested
    def isAnagram_2(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        if len(s_list) == len(t_list):
            if sorted(s_list) == sorted(t_list):
                return True
            else:
                return False
        else:
            return False
