public class Solution {
    public int ShortestDistance(string[] wordsDict, string word1, string word2) {
        
        int maxcount=1000;
        int loc1=1000;
        int loc2=2000;
        
        for(int i=0;i<wordsDict.Length;i++){
           
            if(wordsDict[i]==word1){
                loc1=i;
            }
            if(wordsDict[i]==word2){
                loc2=i;
            }
            if(Math.Abs(loc2-loc1)<maxcount) maxcount=Math.Abs(loc2-loc1);
            if(maxcount==1) return 1;
          
        }
        return maxcount;
        
    }
}