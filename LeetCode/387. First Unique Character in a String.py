# not pretty
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict={}
        array=list(s)
        i=-1
        for char in array:
            i=i+1
            if char in dict:
                dict[char]="F"
            else:
                dict[char]=i
        for value in dict.values():
            if value!="F":
                return value
        return -1

# Leetcode official
import collections

class Solution2:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s) 
        # collections.Counter takes the string and creates a dictionary with a count for each obs.

        # enumarate takes the string and it creates an index idx.
        # then check if the count in the dictionary is 1 and return
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1