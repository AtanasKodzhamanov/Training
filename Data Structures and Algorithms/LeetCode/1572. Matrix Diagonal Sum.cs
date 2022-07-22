public class Solution {
    public int DiagonalSum(int[][] mat) {
        
        int sum=0;
        int j=0;
        for(int i=0;i<mat.Length;i++){
                j=i;           
                sum=sum+mat[i][i] + mat[i][mat.Length-1-i];
                if(mat.Length%2==1 & i==j & i==mat.Length/2) sum=sum- mat[i][j];
                Console.WriteLine(sum);
            
        }
        return sum;
        
    }
}