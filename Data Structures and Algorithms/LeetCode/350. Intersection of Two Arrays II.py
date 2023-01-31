class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        hashmap = {}

        for i in range(len(nums1)):
            hashmap[nums1[i]] = hashmap.get(nums1[i], 0)+1

        for i in range(len(nums2)):
            if hashmap.get(nums2[i]) and hashmap.get(nums2[i]) > 0:
                output.append(nums2[i])
                hashmap[nums2[i]] -= 1
        return output
