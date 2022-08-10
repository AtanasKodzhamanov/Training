public class Solution {
    public bool IsPalindrome(int x) {
      
        Stack stack = new Stack();
        
        foreach(char c in x.ToString()){
            stack.Push(c.ToString());
        }
        foreach(char c in x.ToString()){
            if(stack.Pop().ToString()!=c.ToString()) return false;
        }
        return true;
    }
}