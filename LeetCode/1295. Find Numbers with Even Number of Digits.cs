public class Solution {
    public int FindNumbers(int[] nums) {
        
         int result = 0;
        int j = 0;
        
    for(int i = 0;i < nums.Length; i++){
       j = 0;
        int tmp = nums[i];
        while(tmp!=0){
            tmp /= 10;
            j++;
        }
        if(j%2==0){
            result++;
        }
    }
    return result;
        
    }
}