class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount, tcount = {}, {}
        if len(t) != len(s):
            return False

        for i in range(len(t)):
            tcount[t[i]] = 1 + tcount.get(t[i], 0)
            scount[s[i]] = 1 + scount.get(s[i], 0)

        for i in tcount.keys():
            if tcount[i] != scount.get(i, 0):
                return False
        return True
