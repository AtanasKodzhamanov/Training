public class Solution {
    public int Search(int[] nums, int target) {
        
        int output=-1;
        int lower=0;
        int upper=nums.Length;
        int loc=(lower+upper)/2;
        int count=nums.Length;
        
        while(count>0){
            count=count-1;
            if(loc==0 && nums[loc]==target) return loc;
            if(loc==0 && nums[loc]!=target) return -1;
            
            if(nums[loc]==target) return loc;
            if(nums[loc]<target){
                lower=loc;
            }
            else upper=loc;
            loc=(upper+lower)/2;
            Console.WriteLine(loc);
        }
        
        
        return output;
    }
}