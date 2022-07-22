public class Solution {
    public int MajorityElement(int[] nums) {
        
        int majority=nums.Length/2;
        Console.WriteLine(majority);
        int b=0;
        
        int[] array =new int[nums.Length];
        Array.Sort(nums);
         
        int count=1;
        
        for(int i=0;i<nums.Length-1;i++){
        if( nums[i] ==nums[nums.Length-1]){
            count=count+1;
            
            if(count>majority) return nums[i];
        }         
            if(nums[i]==nums[i+1]){
                count=count+1;   
            }
            else 
            {
                if(count>majority)  {return nums[i]; count=1;b++;}
            }
        }
        
      if(nums.Length==1) return nums[0];
        return -100;
    }
}