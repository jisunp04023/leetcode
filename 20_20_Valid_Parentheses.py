class Solution(object):
    def isValid(self, s):
        stack = []
        
        for i in range(len(s)):
            
            # 여는 괄호 나오면 스택에 push
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
                
            else:
                if len(stack) == 0:
                    return False
                
                popped = stack.pop()
                
                if s[i] == ')' and popped != '(':
                    return False
                elif s[i] == '}'and popped != '{':
                    return False
                elif s[i] == ']'and popped != '[':
                    return False
        
        if len(stack) == 0:
            return True
        
        return False
