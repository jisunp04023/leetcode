from collections import defaultdict

class Solution(object):      
    def findItinerary(self, tickets):
        
        graph = defaultdict(list) # 딕셔너리의 디폴트 value 값을 list로 설정
        
        tickets.sort() # 정렬
        
        for a, b in tickets:
            graph[a].append(b)
        
        
        def dfs(key):
            
            while graph[key]:
                dfs(graph[key].pop(0))
            
            path.append(key)
            
        
        path = []
        dfs('JFK')
                
        
        return path[::-1]
