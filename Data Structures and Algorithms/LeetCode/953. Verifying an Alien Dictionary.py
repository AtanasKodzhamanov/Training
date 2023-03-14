class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {}
        index = 1
        for i in order:
            hashmap[i] = index
            index += 1
        prev = 0
        for i in range(len(words)-1):
            key1 = words[i]
            key2 = words[i+1]
            j = 0

            min_len = min(len(key1), len(key2))
            while j < min_len:

                if hashmap[key1[j]] < hashmap[key2[j]]:
                    break
                if key1[j] == key2[j]:
                    if j == min_len-1:
                        if len(key2) < len(key1):
                            return False
                    j += 1
                else:
                    return False

        return True
