class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1

        while left <= right:
            middle = (left+right)//2

            if nums[middle] == target:
                return middle

            # we are located in the wrong section so we move the pointer to the right
            if nums[middle] >= nums[0] and target < nums[0]:
                left = middle+1
                continue

            # we are located in the wrong section so we move the pointer to the left
            if nums[middle] < nums[0] and target >= nums[0]:
                right = middle-1
                continue

            # perform binary search
            if nums[middle] < target:
                left = middle+1
            else:
                right = middle-1

        return -1
