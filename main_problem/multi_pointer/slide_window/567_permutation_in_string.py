class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        s1 = ''.join(sorted(s1))
        print(s1)
        i = 0
        while i < n2 - n1 + 1:
            if s1 == ''.join(sorted(s2[i: i + n1])):
                return True
            i += 1
        return False
