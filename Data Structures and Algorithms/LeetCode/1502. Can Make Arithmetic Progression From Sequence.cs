public class Solution {
    public bool CanMakeArithmeticProgression(int[] arr) {
        
        Array.Sort(arr);
        int diff=0;
        for(int i=0;i<arr.Length-1;i++){
           if(i==0) diff=arr[i+1]-arr[i];
            if(arr[i+1]-arr[i]!=diff){
                
                 return false;
            }
            
                
        }
        return true;
    }
}