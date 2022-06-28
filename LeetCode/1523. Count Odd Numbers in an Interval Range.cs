public class Solution {
    public int CountOdds(int low, int high) {

    if(high%2==0 & low%2==0){
        return high/2-low/2;
    }
     if(high%2==0 & low%2==1){
        return high/2-low/2;
    }
        else return high/2-low/2+1;
        
    }
}