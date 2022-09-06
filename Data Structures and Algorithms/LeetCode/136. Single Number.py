class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictA={}
        for i in range(len(nums)):
            if nums[i] in dictA:
                dictA[nums[i]]=2
            else:
                dictA[nums[i]]=1
        for key,value in dictA.items():
            if value==1: return key
        return False