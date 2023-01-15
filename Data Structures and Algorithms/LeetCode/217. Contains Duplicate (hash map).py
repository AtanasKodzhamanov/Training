# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """
        Solution: hash map
        Go through the list and start adding nums in a dict.
        If a num already exists, return true.
        """

        dict = {}
        for i in range(len(nums)):
            val = nums[i]
            if val in dict:
                return True
            dict[val] = 1
        return False
