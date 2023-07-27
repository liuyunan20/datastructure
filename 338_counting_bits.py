class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            counter = 0
            while i > 1:
                if i % 2 == 1:
                    counter += 1
                i = i // 2
            if i == 1:
                counter += 1
            result.append(counter)
        return result
