class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        output = ""
        i = 0
        while len(word1) > i and len(word2) > i:
            output += word1[i]
            output += word2[i]
            i += 1

        return output+word2[i:]+word1[i:]
