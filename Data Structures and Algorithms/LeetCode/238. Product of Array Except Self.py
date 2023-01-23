class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        leftprod = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                output[i] = nums[i]
            else:
                output[i] = nums[i]*output[i+1]
        print(output)
        for i in range(len(nums)):
            if i == 0:
                output[i] = output[i+1]
            elif i == len(nums)-1:
                leftprod = leftprod*nums[i-1]
                output[-1] = leftprod
            else:
                leftprod = leftprod*nums[i-1]
                output[i] = output[i+1]*leftprod
        return output
