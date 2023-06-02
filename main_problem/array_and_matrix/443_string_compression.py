from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 1
        result = [chars[0]]
        counter = 1
        while i < n:
            if result[-1] == chars[i]:
                counter += 1
            else:
                if counter > 1:
                    result.append(str(counter))
                    counter = 1
                result.append(chars[i])
            i += 1
        if counter > 1:
            result.append(str(counter))
        result = ''.join(result)
        new_length = len(result)
        for i in range(new_length):
            chars[i] = result[i]
        return new_length
