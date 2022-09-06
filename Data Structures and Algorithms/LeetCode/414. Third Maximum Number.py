class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        initial=float('-inf')
        first,second,third=(float('-inf'),float('-inf'),float('-inf'))
        
        for i in range(len(nums)):
            temp1=first
            temp2=second
            temp3=third
            if nums[i]>first:
                first=nums[i]
                second=temp1
                third=temp2
            elif nums[i]>second and nums[i] != first :
                second=nums[i]
                third=temp2
            elif nums[i]>third and nums[i] != second and nums[i] != first:
                third=nums[i]
    
        if second == initial or third== initial:
            return first
        return third