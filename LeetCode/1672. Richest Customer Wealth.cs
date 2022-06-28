public class Solution {
    public int MaximumWealth(int[][] accounts) {
        
        int wealth=0;
        int maxwealth=0;
        
        for(int i=0;i<accounts.Length;i++){
            wealth=0;
           for(int j=0;j<accounts[i].Length;j++){
            wealth=wealth+accounts[i][j];
            if(maxwealth<wealth) maxwealth=wealth;
        } 
        }
        return maxwealth;
    }
}