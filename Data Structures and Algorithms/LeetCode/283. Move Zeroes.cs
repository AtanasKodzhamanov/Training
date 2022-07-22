public class Solution {
    public void MoveZeroes(int[] nums) {
        
        int zeros=0;
   
        
        for (int i=0;i<nums.Length;i++){
            
            if(i<nums.Length-zeros){
                 nums[i]=nums[i+zeros];
            }
            
            if(i>nums.Length-zeros-1){
                nums[i]=0;
            }
            else if(nums[i]==0){
                zeros++;
                
               Console.WriteLine(zeros);
            }
            
            
            
       if(i<nums.Length-zeros){ if(nums[i]==0) {i=i-1; }}
            
        }
        
    }
}