class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # We can start backwards
        # Compare 6 with 3, place 6 at the end of the array, increase counter. Move pointer to 5.
        # Compare 5 with 3, place 3 at len(arr1)-count
        # Compare 2 with 3, move 2, move pointer 1
        
        if(m==0 and n==1):
            nums1[0]=nums2[0]
            return nums1
        
        pointer1=m-1
        pointer2=n-1
   
        for i in range(n+m-1,-1,-1):
            if pointer2<0: break
            if (nums1[pointer1]>=nums2[pointer2] and pointer1>=0):
                nums1[i]=nums1[pointer1]
                pointer1-=1
            else:
                nums1[i]=nums2[pointer2]
                pointer2-=1
                
        return nums1

        # This is the most optimal solution (based on leetcode solutions)
        # An easier to code solution would be to create a third array and feed it using the other 2.