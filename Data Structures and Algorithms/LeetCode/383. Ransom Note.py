class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictM = {}
        for char in magazine:
            if char in dictM:
                dictM[char] += 1
            else:
                dictM[char] = 1
        for char in ransomNote:
            if char in dictM:
                dictM[char] -= 1
            else:
                return False
        if min(dictM.values()) < 0:
            return False
        else:
            return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = {}

        for i in magazine:
            dictionary[i] = dictionary.get(i, 0)+1

        for i in ransomNote:
            if dictionary.get(i) == None or dictionary[i] == 0:
                return False
            else:
                dictionary[i] -= 1
        return True
