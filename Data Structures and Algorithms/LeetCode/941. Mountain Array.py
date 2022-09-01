class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        #Edge cases are:
        # 10 - only downhill
        # 01 - only uphill
        # 0 - array is of len 1
        # 010 - general case
        # 0110 - flat
        
        # gets rid of 0 and 10 edge cases
        if len(arr)==1:
            return False
        if arr[0]>=arr[1]:
            return False
        
        # with the above code we ensure that we always start uphill. Then we change the flag when we start going downhill. 
        uphill=True
        for i in range(len(arr)-1):
            
            # take care of flat cases
            if arr[i]==arr[i+1]:
                return False

            # make sure you only change directions once and that is downhill
            if uphill==True and arr[i]>arr[i+1]:
                uphill=False
            if uphill==False and arr[i]<arr[i+1]:
                return False
        
        # gets rid of 01 edge case
        if uphill==False:
            return True
        