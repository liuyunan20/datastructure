class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)
        count = 1
        s = ""
        for i in range(length):
            if i + 1 < length and chars[i] == chars[i + 1]:
                count += 1
            else:
                s += chars[i]
                if count != 1:
                    s += str(count)
                count = 1
        i = 0
        while i < len(s):
            chars[i] = s[i]
            i += 1
        chars = chars[:i]

        return len(chars)
