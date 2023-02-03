class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        index1 = index2 = -1
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                if index1 == -1:
                    index1 = i
                elif index2 == -1:
                    index2 = i
                if count > 2:
                    return False
        return s1[index1] == s2[index2] and s1[index2] == s2[index1]
