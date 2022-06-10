from collections import Counter

class Solution(object):
    def dailyTemperatures(self, temperatures):
        
        result = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            
            # 현재 값이 스택의 top 보다 크다면,
            # 스택의 top 인덱스 결과값 = 현재 인덱스 - 스택의 top
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            
            stack.append(i)
        
        return result
