public class Solution {
    public string RemoveDuplicates(string s) {
        
        Stack stack = new Stack();
        StringBuilder full = new StringBuilder();
        
        for (int i=0;i<s.Length;i++){
            if(stack.Count==0) {stack.Push(s[i]); continue;}   
            
            if(stack.Peek().ToString()==s[i].ToString()) stack.Pop();
            else stack.Push(s[i]);
        }
        
        while(stack.Count>0){
            full.Insert(0,stack.Pop());
        }
         return full.ToString();
    }
}