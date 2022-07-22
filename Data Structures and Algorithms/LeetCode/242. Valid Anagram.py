class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dictS={}
        for letter in s:
            if letter in dictS:
                dictS[letter]+=1
            else:
                dictS[letter]=1
        for letter in t:
            if letter in dictS:
                dictS[letter]-=1
        
        if max(dictS.values())>0:
            return False
        else:
            return True