class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = list(ransomNote)
        m = list(magazine)
        for letter in r:
            if letter not in m:
                return False
            m.remove(letter)
        return True
