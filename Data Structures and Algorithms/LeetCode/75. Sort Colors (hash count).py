class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashtable = {}
        for i in nums:
            if hashtable.get(i):
                hashtable[i] += 1
            else:
                hashtable[i] = 1
        print(hashtable)
        loc = 0
        for i in range(3):
            if hashtable.get(i):
                for j in range(hashtable[i]):
                    nums[loc] = i
                    loc += 1
