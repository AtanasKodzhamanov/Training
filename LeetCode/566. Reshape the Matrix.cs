public class Solution {
    public int[][] MatrixReshape(int[][] mat, int r, int c) {
        
        int rows=mat.Length;
        int columns=mat[0].Length;
        int size=columns*rows;
        int[][] array = new int[r][];

      
            
        if(rows==r && columns==c){return mat;}
        if(r*c==size){
            int i=0;
            int j=0;
            int count=0;
            for(int a=0;a<r;a++){
                
                array[a] = new int[c];
                
                for(int b=0;b<c;b++){

                    if(count==columns){i++;j=0;count=0;}
                    
                    array[a][b]=mat[i][j];
                    count++;j++;
            }}
            return array;
        }
        return mat;
    }
}