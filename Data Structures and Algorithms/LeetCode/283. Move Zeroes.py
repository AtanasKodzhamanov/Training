class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
        return nums        

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=-1
        for i in range(len(nums)-1):
            j+=1
            if nums[i]==0:
                if nums[i+1]==0:
                    j-=1
                    continue
                nums[j]=nums[i+1]
                nums[i+1]=0
        return nums        