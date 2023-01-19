class Solution:
    def longestCommonPrefix(strs):
        minword = 200
        output = ""
        for i in strs:
            newlen = len(i)
            if newlen < minword:
                minword = newlen
                minworda = i
        for h in range(len(minworda)):
            letter = minworda[h]
            for j in strs:
                if j[h] != letter:
                    return output
            output += letter
        return output


Solution.longestCommonPrefix(["flower", "flow", "flight"])
