public class Solution {
    public double Average(int[] salary) {
        
       double fa=(double)(salary.Sum()-salary.Min()-salary.Max())/(salary.Count()-2);
        return fa;
    }
}