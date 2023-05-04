class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        num_col = {0: "Z", 1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F",
         7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L", 13: "M",
         14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T",
         21: "U", 22: "V", 23: "W", 24: "X", 25: "Y"}
        n1 = columnNumber
        s = []
        while n1 > 0:
            n2 = n1 % 26
            s.append(num_col[n2])
            n1 = n1 // 26
            if n2 == 0:
                n1 -= 1
        return "".join(s[::-1])
