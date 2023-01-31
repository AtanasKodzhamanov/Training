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


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)-1
        left = 0
        right = len(nums)-1
        temp = ""
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1
        left = 0
        right = k

        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1
        print(nums)
        left = k+1
        right = len(nums)-1

        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1
