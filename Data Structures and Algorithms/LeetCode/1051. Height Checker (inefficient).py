class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=heights.copy()
        expected.sort()
        
        mismatch=0
        
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                mismatch+=1
        return mismatch
        
        