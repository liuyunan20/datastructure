import string


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n = len(abbr)
        i = 0
        word_ab = []
        number_start = False
        while i < n:
            while i < n and abbr[i] not in string.digits:
                word_ab.append(abbr[i])
                i += 1
            if i == n:
                break
            if not number_start and abbr[i] == "0":
                return False
            number_start = True
            num = []
            while i < n and abbr[i] in string.digits:
                num.append(abbr[i])
                i += 1
            num = int("".join(num))
            if num != 0:
                word_ab.append(num)
            else:
                return False
            number_start = False
        n = len(word)
        i = 0
        while i < n and word_ab:
            x = word_ab.pop(0)
            if isinstance(x, int):
                i += x
            else:
                if word[i] != x:
                    return False
                i += 1
        return True if i == n and not word_ab else False
