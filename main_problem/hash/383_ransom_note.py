class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = {}
        for i in range(len(ransomNote)):
            r.setdefault(ransomNote[i], 0)
            r[ransomNote[i]] += 1
        m = {}
        for i in range(len(magazine)):
            m.setdefault(magazine[i], 0)
            m[magazine[i]] += 1
        for letter in r:
            if not m.get(letter) or m[letter] < r[letter]:
                return False
        return True
