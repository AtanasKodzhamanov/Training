class Solution:
    def freqAlphabets(self, s: str) -> str:
        output = ""
        dic = collections.defaultdict(str)
        for i, v in enumerate(string.ascii_lowercase):
            dic[str(i+1)] = v

        i = len(s)-1
        while i >= 0:
            if s[i] == "#":
                num = s[i-2]+s[i-1]
                output = dic[num]+output
                i -= 3
            else:
                output = dic[s[i]]+output
                i -= 1
        return output
