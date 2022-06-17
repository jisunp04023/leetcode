class Solution(object):      
    def combine(self, n, k):
        
        def dfs(elements, start, k):
            # path 길이가 k가 되었다면 결과에 추가
            if not k:
                result.append(elements[:])
                return
            
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()
                
        result = []
        dfs([], 1, k)
        
        return result
