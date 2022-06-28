public class Solution {
    public int RomanToInt(string s) {
    
        int final=0;
        int flag=0;
     
        for(int i=0;i<s.Length;i++){
        
            if(flag ==0)
            {   
                if(s[i].ToString()=="I")
                {
                    if(i+2 <=s.Length)
                        {
                    if(s[i+1].ToString()=="V") {final=final+4; flag=1;}
                    else if(s[i+1].ToString()=="X") {final=final+9; flag=1;}
                    else final=final+1; 
                        }
                    else final=final+1; 
                }
                if(s[i].ToString()=="X")
                {
                    if(i+2 <=s.Length)
                        {
                    if(s[i+1].ToString()=="L") {final=final+40; flag=1;}
                    else if(s[i+1].ToString()=="C") {final=final+90; flag=1;}
                    else final=final+10; 
                        }
                    else final=final+10; 
                }
                if(s[i].ToString()=="C")
                {
                    if(i+2 <=s.Length)
                        {
                    if(s[i+1].ToString()=="D") {final=final+400; flag=1;}
                    else if(s[i+1].ToString()=="M") {final=final+900; flag=1;}
                    else final=final+100; 
                        }
                    else final=final+100; 
                }
                if(s[i].ToString()=="V") final=final+5;
                if(s[i].ToString()=="L") final=final+50;
                if(s[i].ToString()=="D") final=final+500;
                if(s[i].ToString()=="M") final=final+1000;
             
            }
            else flag=0;
        } 
        
       return final;
        
     }
        
    }