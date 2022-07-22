class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        deb=0
        for i in range(len(digits)-1,-1,-1):
            if digits[i]+1==10:
                digits[i]=0
                if i==0:
                    digits.insert(0,1)
                    return digits
            else: 
                digits[i]=digits[i]+1
                return digits 
            
        return digits