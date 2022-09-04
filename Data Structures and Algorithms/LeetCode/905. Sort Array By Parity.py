class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        # A few examples and edge cases
        # [3,3]
        # [2,2]
        # [3]
        # [2]
        # [3,4,2] -> [2,4,3]
        
        # We want O(N) and in-place
        
        # Start iterating through the array. If you encounter an even number replace it with the first number in the array. Keep a counter of how many have been replaced.
        
        temp=0
        count=0
        
        for i in range(len(nums)):
            if nums[i]%2 ==0:
                temp=nums[count]
                nums[count]=nums[i]
                nums[i]=temp
                count+=1
            
        return nums
                
                
                