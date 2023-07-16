class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    isConnected[i][j] = 0
                    isConnected[j][i] = 0
                    isConnected[i][i] = 0
                    isConnected[j][j] = 0
                    provinces += 1
                    prv = {i, j}
                    while prv:
                        p = prv.pop()
                        for q in range(n):
                            if q != p and isConnected[p][q] == 1:
                                prv.add(q)
                                isConnected[p][q] = 0
                                isConnected[q][p] = 0
                                isConnected[q][q] = 0
        return provinces
