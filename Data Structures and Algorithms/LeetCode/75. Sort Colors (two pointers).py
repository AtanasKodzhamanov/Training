class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rightP = len(nums)-1
        leftP = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums[i] = nums[leftP]
                nums[leftP] = 0
                leftP += 1
            if nums[i] == 2:
                nums[i] = nums[rightP]
                nums[rightP] = 2
                rightP -= 1
                i -= 1  # this is the edge case where the rightP is a 0. We need to check it again
            i += 1
            if i > rightP:  # if i is greater than rightP, we have already checked all the 2s and we can break
                break
