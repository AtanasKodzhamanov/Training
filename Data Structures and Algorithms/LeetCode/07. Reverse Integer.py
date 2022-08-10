class Solution:
    def reverse(self, x: int) -> int:
        output=[]
        neg=False
        if(x<0):
            neg=True
            x=abs(x)
        for char in str(x):
            output.insert(0,char)
        out=int(''.join(output))
        if(out>=2**31-1):
            return 0
        if(neg==True):
            return -out
        return out