class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxlength = 0
        for i in range(len(s)):
            while s[i] in s[left:i]:
                left += 1
            if i-left+1 > maxlength:
                maxlength = i-left+1
        return maxlength


O(n) O(1)
