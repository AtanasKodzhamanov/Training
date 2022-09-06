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


# Neater

    def thirdMax(self, nums):
        v = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            if num not in v:
                if num > v[0]:   v = [num, v[0], v[1]]
                elif num > v[1]: v = [v[0], num, v[1]]
                elif num > v[2]: v = [v[0], v[1], num]
        return max(nums) if float('-inf') in v else v[2]