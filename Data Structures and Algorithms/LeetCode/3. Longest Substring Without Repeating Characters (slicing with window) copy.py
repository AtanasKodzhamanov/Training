class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxlength = 0
        string = ""
        for i in range(len(s)):
            while s[i] in string:
                left += 1
                string = s[left:i]
            if s[i] not in string:
                string = s[left:i+1]
            if len(string) > maxlength:
                maxlength = len(string)
        return maxlength


# O(n) O(n)
