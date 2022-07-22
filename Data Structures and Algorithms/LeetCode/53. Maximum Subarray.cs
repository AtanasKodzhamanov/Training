public class Solution {
    public int MaxSubArray(int[] nums) {
        int maxsum=-100000;
        int sum=0;

        
        
        for(int i=0;i<nums.Length;i++){
            sum=sum+nums[i];
            if(sum>=maxsum) {maxsum=sum;}
            if(sum<0) sum=0;
        }

        return maxsum;
    }
}