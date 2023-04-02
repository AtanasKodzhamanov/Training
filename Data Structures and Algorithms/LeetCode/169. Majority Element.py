class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer moore algo

        count = 0
        result = 0

        for n in nums:
            if count == 0:
                result = n
            if n == result:
                count += 1
            else:
                count -= 1
        return result


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
        return max(hashmap, key=hashmap.get)
