class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setNums=set(nums)
        if len(setNums)<len(nums):
            return True
        return False