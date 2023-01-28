class Solution:
    def isHappy(self, n: int) -> bool:
        num=0
        i=0
        setA=set()
        while True:
            for char in str(n):
                num+=int(char)**2
            n=str(num)
            
            if num in setA:
                return False
            setA.add(num)

            if num==1: 
                return True
            num=0