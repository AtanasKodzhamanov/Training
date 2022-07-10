class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s = ''.join(ch for ch in s if ch.isalnum())
        print(s)
        if s==s[::-1]:
            return True
        return False