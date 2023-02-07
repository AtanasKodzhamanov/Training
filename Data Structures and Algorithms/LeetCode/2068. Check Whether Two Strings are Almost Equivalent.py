class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        hashmap = {}
        hashmap2 = {0: 0}
        x = 0

        for i in word1:
            hashmap[i] = hashmap.get(i, 0)+1

        for i in word2:
            if hashmap.get(i):
                hashmap[i] -= 1
            else:
                hashmap2[i] = hashmap2.get(i, 0)+1
        if max(max(hashmap.values()), max(hashmap2.values())) > 3:
            return False
        return True
