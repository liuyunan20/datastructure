class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        for letter in list(s):
            freq.setdefault(letter, 0)
            freq[letter] += 1
        freq = sorted(freq.items(), key=lambda x: -x[1])
        if freq[0][1] > sum([x[1] for x in freq[1:]]) + 1:
            return ''
        result = [freq[0][0] for _ in range(freq[0][1])]
        string = ''
        for letter, num in freq[1:]:
            string += letter * num
        string = list(string)
        while True:
            for i in range(len(result)):
                if not string:
                    return ''.join(result)
                result[i] += string.pop(0)
