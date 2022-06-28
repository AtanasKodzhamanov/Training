public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        
        string oldpref="";
        string newpref="";
        string word="";
        string prefix="";
        int j=0;
        int min=110;
    
        while(true){
            
        prefix+= oldpref;
        for(int i=0;i<strs.Length;i++){
            
            
            word=strs[i]; if(word.Length==0) return ""; 
            if(j>=word.Length) return prefix;
            newpref=word[j].ToString();
            
            if(i==0){oldpref=newpref;}
        
            if(oldpref==newpref){oldpref=newpref;}
            if(oldpref!=newpref){return prefix;}
            
        }
            j++;
        }
        
        
    }
}