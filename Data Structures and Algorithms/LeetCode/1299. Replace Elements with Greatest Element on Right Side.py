class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxe=-1
        newmax=-1
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>=maxe:
                newmax=arr[i]
            arr[i]=maxe
            maxe=newmax
        return arr