public class Solution {
    public string Interpret(string command) {
       
 
        string prev="";
        string final="";
        
        foreach (char i in command){
            
            if(i.ToString()=="G") final=final+"G";
            if(i.ToString()==")")
            {
                if(prev=="l") final=final+"al";
                else final=final+"o";
            }
            
            prev=i.ToString();
            
            
        }
        return final;
    }
}