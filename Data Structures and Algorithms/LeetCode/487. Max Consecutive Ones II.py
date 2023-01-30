class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = -1
        flipped = False
        maxcons = 0
        curcons = 0
        # [1,0,1,1,0,1]
        # [1,0,0,0,1]
        for i in range(len(nums)):
            if nums[i] == 0:
                curcons = i-left-1
                left = i

            curcons += 1
            maxcons = max(curcons, maxcons)

        return maxcons
