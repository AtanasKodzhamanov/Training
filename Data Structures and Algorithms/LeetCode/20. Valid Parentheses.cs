public class Solution {
    public bool IsValid(string s) {
        
        int big=0;
        int med=0;
        int small=0;
        int cur=0;
        int last=0;
         Stack stack = new Stack();
        if(s.Length==1)return false;
        
       for(int i=0;i<s.Length;i++){
           
           if(s[i].ToString()=="["){              
                stack.Push("[");
           }
           if(s[i].ToString()=="]"){     
               if(stack.Count==0) return false;
               if (stack.Pop() !="[") return false;
           }
           if(s[i].ToString()=="{"){              
               stack.Push("{");
           }
           if(s[i].ToString()=="}"){  
               if(stack.Count==0) return false;
             if (stack.Pop() !="{") return false;
           }
           if(s[i].ToString()=="("){              
                stack.Push("(");
           }
           if(s[i].ToString()==")"){ 
               if(stack.Count==0) return false;
           if (stack.Pop() !="(") return false;
           }
          
        
       }   
        if(stack.Count>0) return false;
     return true;
        
    }
}