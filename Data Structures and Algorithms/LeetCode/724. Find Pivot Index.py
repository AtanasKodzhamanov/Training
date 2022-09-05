# Dictionaries
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        runsum=0
        leftD={}
        rightD={}
        for i in range(len(nums)):
            leftD[i]=runsum
            runsum+=nums[i]
        runsum=0
        for i in range(len(nums)-1,-1,-1):
            rightD[i]=runsum
            runsum+=nums[i]
        print(leftD)
        print(rightD)
        for i in range(len(nums)):
            if leftD[i]==rightD[i]:
                return i
        return -1
        
# using sum()
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumar=sum(nums)
        runsum=0
        for i in range(len(nums)):
            if(runsum==sumar-runsum-nums[i]):
                return i
            runsum+=nums[i]
        return -1