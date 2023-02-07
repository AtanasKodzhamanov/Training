class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tableS = {}
        for i in s:
            tableS[i] = tableS.get(i, 0)+1

        for i in t:
            if tableS.get(i) and tableS[i] > 0:
                tableS[i] = tableS.get(i, 0)-1
            else:
                return i
