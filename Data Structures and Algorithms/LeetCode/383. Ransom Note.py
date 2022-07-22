class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictM={}
        for char in magazine:
            if char in dictM:
                dictM[char]+=1
            else:
                dictM[char]=1
        for char in ransomNote:
            if char in dictM:
                dictM[char]-=1
            else:
                return False
        if min(dictM.values())<0:
            return False
        else:
            return True