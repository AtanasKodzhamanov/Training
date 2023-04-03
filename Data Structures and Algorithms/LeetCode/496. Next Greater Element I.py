class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexDict = {v: i for i, v in enumerate(nums1)}
        result = [-1]*len(nums1)

        for i in range(len(nums2)):
            value = nums2[i]
            if value not in indexDict:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > value:
                    result[indexDict[value]] = nums2[j]
                    break
        return result
