class Solution:
    def reverseWords(self, s: str) -> str:
         return " ".join("".join(list(s)[::-1]).split()[::-1])
