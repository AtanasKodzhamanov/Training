public class Solution {
    public bool CanPlaceFlowers(int[] flowerbed, int n) {
        
        if (n==0) return true;
        
        if(flowerbed.Length==1){
            if(n==1 & flowerbed[0]==0) return true; else return false;
        }
             if(flowerbed.Length==2){
            if(n==1 & flowerbed[0]==0 & flowerbed[1]==0) return true; else return false;
        }    

            for(int i=1;i<flowerbed.Length-1;i++){
           if(flowerbed[0]==0 && flowerbed[1]==0) 
            { flowerbed[0]=1;
                n=n-1;}
            
            if(flowerbed.Length>2) if(flowerbed[i-1]==0 & flowerbed[i]==0 & flowerbed[i+1]==0){
                flowerbed[i]=1;
                n=n-1;
            }}
        
        if(flowerbed[flowerbed.Length-1]==0 & flowerbed[flowerbed.Length-2]==0) n=n-1;
        if(n<=0) return true;
        else return false;
 
    }
}