class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        result=[0]*len(nums)
        leftPointer=0
        rightPointer=len(nums)-1    

        #sort the array using 2 pointers
        for i in range(len(nums)):
            ln=nums[leftPointer]**2
            rn=nums[rightPointer]**2
            index=len(nums)-i-1
            
            if ln>=rn:
                result[index]=ln
                leftPointer+=1
            else:
                result[index]=rn
                rightPointer-=1

        return result

#Key: as the input comes pre-sorted we can use that together with 2 pointers to sort the array