class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexDict = {v: i for i, v in enumerate(nums1)}
        result = [-1]*len(nums1)

        stack = []

        for i in range(len(nums2)):
            value = nums2[i]
            while stack and value > stack[-1]:
                pop = stack.pop()
                if pop in indexDict:
                    result[indexDict[pop]] = value
            if value in indexDict:
                stack.append(value)
        return result
