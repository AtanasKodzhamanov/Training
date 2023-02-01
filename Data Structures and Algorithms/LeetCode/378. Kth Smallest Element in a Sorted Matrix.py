class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        numlist = []
        for nums in matrix:
            for i in nums:
                numlist.append(i)

        numlist = [-x for x in numlist]
        heapq.heapify(numlist)

        while len(numlist) > k:
            heapq.heappop(numlist)
        return -numlist[0]
