public class Solution {
    public int SumOddLengthSubarrays(int[] arr) {
        
        
        if(arr.Length==2) return arr[1]+arr[0];
        if(arr.Length==1) return arr[0];
        
        int runningsum=0;
        int total=0;
        
        for(int i=0;i<arr.Length;i++){
            
            
            
            for(int j=i;j<arr.Length;j++){
                runningsum=runningsum+arr[j];
                if((j-i)%2==0) total=total+runningsum;
                Console.WriteLine(runningsum + " and total:" +total);
            }
            runningsum=0;

        }
        return total;
    }
}