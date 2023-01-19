class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        spointer = 0
        if len(s) == 0:
            return True
        for i in t:
            if i == s[spointer]:
                spointer += 1
            if spointer == len(s):
                return True
        return False
