class Solution:
    def countAndSay(self, n: int) -> str:
        def say(digits):
            result = []
            i = 0
            while i < len(digits):
                temp = [digits[i]]
                while i < len(digits) - 1 and digits[i] == digits[i + 1]:
                    temp.append(digits[i + 1])
                    i += 1
                result.append(str(len(temp)))
                result.append(digits[i])
                i += 1
            return "".join(result)

        if n == 1:
            return "1"
        if n == 2:
            return "11"
        return say(self.countAndSay(n - 1))
