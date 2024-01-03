class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result = []
        new = list(score)
        new.sort(key= lambda x: -x)
        for s in score:
            rank = new.index(s) + 1
            if rank == 1:
                result.append("Gold Medal")
            elif rank == 2:
                result.append("Silver Medal")
            elif rank == 3:
                result.append("Bronze Medal")
            else:
                result.append(str(rank))
        return result
