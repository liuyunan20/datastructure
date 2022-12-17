class Solution:
    def longestSubstring_wrong(self, s: str, k: int) -> int:
        # wrong answer with test case "ababacb" k = 3
        if len(s) == 1 and k == 1:
            return 1
        freq = {}
        for letter in s:
            freq.setdefault(letter, 0)
            freq[letter] += 1
        i = 0
        n = len(s)
        j = n - 1
        while i < j:
            if min(freq.values()) >= k:
                return j - i + 1
            if freq[s[i]] < k:
                freq[s[i]] -= 1
                if freq[s[i]] == 0:
                    del freq[s[i]]
                i += 1
            if freq[s[j]] < k:
                freq[s[j]] -= 1
                if freq[s[j]] == 0:
                    del freq[s[j]]
                j -= 1
        return 0

    def longestSubstring_wrong2(self, s: str, k: int) -> int:
        if len(s) == 1 and k == 1:
            return 1
        freq = {}
        letter_more = set()
        for letter in s:
            freq.setdefault(letter, 0)
            freq[letter] += 1
            if freq[letter] >= k:
                letter_more.add(letter)
        letter_less = set(list(s)) - letter_more

        i = 0
        n = len(s)
        j = n - 1
        while i < j:
            if min(freq.values()) >= k:
                return j - i + 1
            if freq[s[i]] < k:
                freq[s[i]] -= 1
                if freq[s[i]] == 0:
                    del freq[s[i]]
                i += 1
            elif freq[s[j]] < k:
                freq[s[j]] -= 1
                if freq[s[j]] == 0:
                    del freq[s[j]]
                j -= 1
            else:
                i =
        return 0
