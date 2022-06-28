public class Solution {
    public int NearestValidPoint(int x, int y, int[][] points) {
        
        int output=-1;
        int mancur=100000;
        int manmin=100000;
        int minr=10000;
        int valid=0;
     
        for(int r=points.GetLength(0)-1;r>=0;r--){
                if(points[r][0]==x || points[r][1]==y)
                {
                    valid++;
                    mancur=Math.Abs(x-points[r][0])+Math.Abs(y-points[r][1]);
                    if (mancur<=manmin) {manmin=mancur; minr=r;}
                }
                
                
 
            }
        if(valid==0) return -1;
            return minr;
        }

    }