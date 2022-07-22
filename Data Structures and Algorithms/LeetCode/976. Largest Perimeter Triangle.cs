public class Solution {
    public int LargestPerimeter(int[] nums) {
        Array.Sort(nums);
        Array.Reverse(nums);
        int pem=0;
        for(int i=0;i<nums.Length-2;i++){
            if(nums[0+i]>=nums[1+i]+nums[2+i]) pem=0;
            else {pem=nums[0+i]+nums[1+i]+nums[2+i];
            return pem;}
        }
        return pem;
     
    
    }
}