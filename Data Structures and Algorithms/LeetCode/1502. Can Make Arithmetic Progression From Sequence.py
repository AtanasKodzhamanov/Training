class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        minnum = min(arr)
        maxnum = max(arr)
        difference = (maxnum-minnum)/(len(arr)-1)

        total = minnum
        for i in range(len(arr)-1):
            if total not in arr:
                return False
            total += difference
        return True
