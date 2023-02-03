class Solution:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = len(s)-1
        output = ""
        for i in s.split(" "):
            for j in range(len(i)-1, -1, -1):
                output += i[j]
            output += " "
        return output[:-1]
