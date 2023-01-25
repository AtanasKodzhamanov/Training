from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hashmap = defaultdict(list)
        output = set()
        for i in range(len(s)):
            hashmap[s[i]].append(i)
        for key in hashmap:
            for i in range(min(hashmap[key])+1, max(hashmap[key])):
                output.add(key+s[i]+key)
        return len(output)
