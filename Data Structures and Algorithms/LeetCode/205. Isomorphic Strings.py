class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        hashmap1 = {}
        hashmap2 = {}

        for i in range(len(s)):
            if s[i] not in hashmap1:
                hashmap1[s[i]] = t[i]
            else:
                if hashmap1[s[i]] != t[i]:
                    return False

        for i in range(len(s)):
            if t[i] not in hashmap2:
                hashmap2[t[i]] = s[i]
            else:
                if hashmap2[t[i]] != s[i]:
                    return False
        return True

# The tricky part is knowing that it has to  map both ways. No two characters should map to the same character!
