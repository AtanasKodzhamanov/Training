class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        num = float('inf')

        for i in nums:
            if abs(i) < abs(num):
                num = i
            if abs(i) == abs(num):
                if i > num:
                    num = i
        return num
