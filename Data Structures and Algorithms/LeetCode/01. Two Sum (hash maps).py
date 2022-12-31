# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        Solution:
        1. Create a dictionary that holds the entire nums array. Have the nums value as the key and the nums index as the dict value. You don't need to do this as a separate step. You can start iterating through the array and checking at the same time. 
        2. Calculate the number you need to find given your position in the array. 
        - target - nums[i] = X
        3. Check if X exists in the hash map. 
        4. If it does output i and the hash key. 
        
        O(n) memory and speed
        """

        dict = {}  # put i as a key and nums index as dict value
        # enumerate takes the index and the value - i, nums[i].

        for i, val in enumerate(nums):
            wanted = target-val
            if wanted in dict:
                return [dict[wanted], i]
            dict[val] = i
