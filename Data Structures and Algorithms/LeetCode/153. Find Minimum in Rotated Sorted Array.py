class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums)-1
        first = nums[0]
        last = nums[-1]

        if first <= last:
            return first
        # two possibilities, we are in the left or the right part.

        # if we are in the left part we need to go right. Use first number to determine where you are

        while left <= right:
            middle = (left+right)//2

            if nums[middle] >= first:
                left = middle+1
            else:
                right = middle-1

        return nums[left]
