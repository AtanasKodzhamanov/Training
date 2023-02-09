class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        middle = 0
        output = []
        if len(nums) == 0:
            return [-1, -1]
        while left <= right:
            middle = (left+right)//2
            if nums[middle] >= target:
                right = middle-1
            else:
                left = middle+1
        print(left)
        output.append(left)
        if left > len(nums)-1 or nums[left] != target:
            return [-1, -1]

        left = 0
        right = len(nums)-1
        middle = 0

        while left <= right:
            middle = (left+right)//2
            if nums[middle] > target:
                right = middle-1
            else:
                left = middle+1
        output.append(right)

        return output
