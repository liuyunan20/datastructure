from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def creat_line(l, c):
            n = len(l)
            if n == 1:
                return l[0] + " " * (maxWidth - len(l[0]))
            if n == 2:
                return l[0] + " " * (maxWidth - c + n) + l[1]
            r = (maxWidth - c + n) % (n - 1)
            d = (maxWidth - c + n) // (n - 1)
            if r == 0:
                space = " " * d
                return space.join(l)
            res = ""
            for i in range(n - 1):
                if r > 0:
                    res += l[i] + " " * (d + 1)
                    r -= 1
                else:
                    res += l[i] + " " * d
            return res + l[-1]

        result = []
        i = 0
        line = []
        counter = 0
        while i < len(words):
            if counter + len(words[i]) > maxWidth:
                result.append(creat_line(line, counter))
                line = []
                counter = 0
            line.append(words[i])
            counter += len(words[i]) + 1
            i += 1
        last_line = " ".join(line)
        result.append(last_line + " " * (maxWidth - len(last_line)))
        return result
