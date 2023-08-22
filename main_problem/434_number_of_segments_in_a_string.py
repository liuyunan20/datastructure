class Solution:
    def countSegments(self, s: str) -> int:
        s = s.split(" ")
        length = 0
        for seg in s:
            if seg and seg != " ":
                length += 1
        return length
