class Solution:
    def check(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(len(nums)):
            if nums[i-1] > nums[i]:
                cnt += 1
        return cnt <= 1

# Must have a non-decreasing array and may be rotated at some pivot unknown to you beforehand.
# The trick here is that nums[i-1] checks the end of the array at the start, so if the number is larger it will increase the counter
# We would expect to see only one increase in the counter if it is sorted and rotated.
