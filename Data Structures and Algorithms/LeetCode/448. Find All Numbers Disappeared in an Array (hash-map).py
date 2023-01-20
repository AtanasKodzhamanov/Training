class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for i in range(1, len(nums)+1):
            hashmap[i] = 0
        for i in nums:
            hashmap[i] = 1
        return {k: v for k, v in hashmap.items() if v == 0}
