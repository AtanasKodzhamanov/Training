class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, k-1
        mindiff = float("inf")

        while right < len(nums):
            curdiff = nums[right]-nums[left]
            mindiff = min(curdiff, mindiff)
            left += 1
            right += 1

        return mindiff
