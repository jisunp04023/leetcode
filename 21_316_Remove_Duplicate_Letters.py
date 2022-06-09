from collections import Counter

class Solution(object):
    def removeDuplicateLetters(self, s):

        counter = Counter(s) # 각 문자당 개수를 저장
        
        stack = []
        
        for i in s:
            counter[i] -= 1
            
            # 이미 있는 문자라면 continue
            if i in stack:
                continue
            
            # 스택이 비어있지 않고,
            # 현재 문자가 스택의 마지막 문자보다 앞선 문자이며,
            # 스택의 마지막 문자가 뒤에 또 나온다면,
            while stack and stack[-1] > i and counter[stack[-1]] > 0:
                stack.pop() # 문자를 뺀다!
            
            # 나머지 경우에는 스택에 문자 추가
            stack.append(i)
            
        return ''.join(stack)
