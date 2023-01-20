class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        present = set(nums)
        output = []
        for i in range(1, len(nums)+1):
            if i not in present:
                output.append(i)
        return output

# Using list comprehension


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        present = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in present]
