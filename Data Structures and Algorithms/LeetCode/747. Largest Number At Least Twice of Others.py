class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest=max(nums)
        index=-1
        for i in range(len(nums)):
            if largest==nums[i]:
                index=i
            elif largest<nums[i]*2:
                return -1
        return index