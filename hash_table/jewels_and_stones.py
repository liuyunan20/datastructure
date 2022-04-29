class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        jewel_type = set(list(jewels))
        for stone in list(stones):
            if stone in jewel_type:
                result += 1
        return result
