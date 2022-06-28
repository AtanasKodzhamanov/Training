public class Solution {
    public bool IsHappy(int n) {
        int count=0;
        string ns = "";
        int newn=0;
        
        while(n != 1){
            count++;
            ns=n.ToString();
           foreach(char i in ns){
                newn= newn+ (int)Char.GetNumericValue(i)*(int)Char.GetNumericValue(i);
            }
            n=newn;
            newn=0;
            
            
            if(count>1000) return false;
        }
        return true;  
    }
}