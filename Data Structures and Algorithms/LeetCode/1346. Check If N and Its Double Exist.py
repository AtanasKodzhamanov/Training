class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dictr={}
        zero=0
        for i in range(len(arr)):
            dictr[i]=arr[i]*2
            if arr[i]==0:
                zero+=1
                if zero==2:
                    return True
        for i in range(len(arr)):
            if arr[i] in dictr.values() and arr[i] !=0:
                return True