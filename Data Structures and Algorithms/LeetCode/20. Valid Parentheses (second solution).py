class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for val in list(s):
            if len(stack)==0:
                stack.append(val)
            elif len(stack)>0:
                if stack[-1]=="(" and val==")":
                    stack.pop()
                elif stack[-1]=="[" and val=="]":
                    stack.pop()
                elif stack[-1]=="{" and val=="}":
                    stack.pop()
                else:
                    stack.append(val)
                    
        if len(stack)==0:
            return True
        return False