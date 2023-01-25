class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftP = 0
        rightP = len(s)-1
        s = s.lower()
        while leftP <= rightP:
            if s[leftP].isalnum() == False:
                leftP += 1
                continue
            if s[rightP].isalnum() == False:
                rightP -= 1
                continue
            if s[leftP] != s[rightP]:
                return False
            leftP += 1
            rightP -= 1

        return True
