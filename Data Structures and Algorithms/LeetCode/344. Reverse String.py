class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        temp=0
        for i in range(int(len(s)/2)):
            temp=s[i]
            s[i]=s[len(s)-i-1]
            s[len(s)-i-1]=temp
        return s