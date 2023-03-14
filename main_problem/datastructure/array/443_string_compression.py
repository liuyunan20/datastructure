from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        counter = 1
        n = len(chars)
        while i < n - 1:
            if chars[i] == chars[i + 1]:
                if counter != 1:
                    chars[i] = ""
                counter += 1
                if i == n - 2:
                    chars[i + 1] = str(counter)

            elif counter != 1:
                chars[i] = str(counter)
                counter = 1
            i += 1
        s = "".join(chars)
        for _ in range(n):
            chars.pop()
        for char in list(s):
            chars.append(char)
        return len(chars)
