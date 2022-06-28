public class Solution {
    public bool AreAlmostEqual(string s1, string s2) {
        
        int count=0;
        string sl1="ab";
        string sl2="bb";
        string sl11="cc";
        string sl22="dd";
        for(int i=0;i<s1.Length;i++)
        {
            if(s1[i]!=s2[i])
            {
                count++;
                if(count==1){
                    sl1=s1[i].ToString();
                sl2=s2[i].ToString();}
                else{
                    sl11=s1[i].ToString();
                sl22=s2[i].ToString();
                }
            }
            
        }
        if(count>2) {return false;}
            if(sl1==sl22 && sl2==sl11) return true;
        if(count==0) return true;
            else return false;
    }       
}