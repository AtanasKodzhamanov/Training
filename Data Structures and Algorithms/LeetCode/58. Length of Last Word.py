class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.split()[-1])
        c = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if c >= 1:
                    return c
            else:
                c = c+1
        return c
