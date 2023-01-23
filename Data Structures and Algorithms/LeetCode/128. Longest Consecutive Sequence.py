class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashtable = set()  # can directly add to set. No point iterating through list
        longest = 0
        newlong = 1
        j = 1
        for i in nums:
            hashtable.add(i)
        for i in nums:
            if i-1 in hashtable:
                continue
            while i+j in hashtable:
                j += 1
                newlong += 1
            j = 1
            if newlong >= longest:
                longest = newlong
            newlong = 1
        return longest


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
