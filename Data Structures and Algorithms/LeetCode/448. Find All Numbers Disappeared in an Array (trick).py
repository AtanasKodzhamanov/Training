class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            index = abs(i)
            nums[index-1] = abs(nums[index-1])*-1
        return [i for i in range(1, len(nums)+1) if nums[i-1] > 0]
