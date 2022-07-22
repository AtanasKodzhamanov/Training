class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output=[]
        for element in nums1:
            if element in nums2 and element not in output:
                output.append(element)
        return output


# To solve the problem in linear time, use the structure set.
# It provides in/contains operation in O(1) time in average case.

#Efficient 1 
# set_intersection(set2, set1)

#Efficient 2
# return list(set(nums2)-(set(nums2) - set(nums1)))

#Efficient 3
# set1 = set(nums1)
# set2 = set(nums2)
# return list(set2 & set1)

