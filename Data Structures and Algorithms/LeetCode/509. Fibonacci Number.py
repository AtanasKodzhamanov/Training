class Solution:
    def fib(self, n: int) -> int:
        
        # F(0)=0
        # F(1)=1
        # F(2)= F(1)+F(0)
        
        # avoid the recursive trap

        if n <2: return n
        
        prev1,prev2,cur=[1,0,0]
        
        for i in range(1,n):
            cur=prev1+prev2 
            prev2, prev1=[prev1,cur]
            
        return cur