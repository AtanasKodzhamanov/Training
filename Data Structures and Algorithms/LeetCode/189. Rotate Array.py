class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, k):
            nums.insert(0, nums.pop(len(nums)-1))


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        firsthalf = nums[-k:]
        second = nums[:len(nums)-k]
        j = 0
        for i in range(len(firsthalf)):
            nums[i] = firsthalf[i]
        for i in range(len(firsthalf), len(nums)):
            nums[i] = second[j]
            j += 1
