class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        arr2 = sorted(arr2)
        counter = 0

        for num in arr1:
            i = 0
            j = len(arr2)-1

            while i <= j:
                mid = (j+i)//2

                val = abs(num - arr2[mid])
                if val <= d:
                    counter += 1
                    break
                elif arr2[mid] < num:
                    i = mid+1
                else:
                    j = mid-1

        return len(arr1)-counter
