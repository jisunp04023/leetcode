from collections import defaultdict
import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        # 1. src부터 dst까지 경로가 존재하는가?
        # 2. 경유지 k개 이하의 경로가 존재하는가?
        # 3. 조건 1,2 만족 하는 경로 중 소요시간이 가장 짧은 경로는?
        
        graph = defaultdict(list)
        
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # 방문한 노드를 기록하여 time limit exceeded 발생을 막는다!!!
        visited = {}
        
        # [다음노드까지 총 소요시간, 다음노드, 가능한 남은 경유지 수]
        Q = [(0, src, k)]
        
        while Q:
            price, node, cnt = heapq.heappop(Q)
            
            # 소요시간이 짧은 것부터 꺼내오기 때문에 바로 정답 리턴해도 됨
            if node == dst:
                return price
            
            # 경유할 수 있는 노드 수가 남아있고,
            # 경우 1 -> 방문하지 않은 노드라면 남은 경유지 수 기록
            # 경우 2 -> 방문한 노드지만 남아있는 경유지의 개수가 기록된 것 보다 더 많으면 새로운 경로 있을 수 있으므로 cnt값 더 큰 수로 갱신
            if cnt >= 0 and (node not in visited or visited[node] < cnt):
                visited[node] = cnt # 방문한 노드를 기록
                for v, w in graph[node]:
                    alt = price + w # 총 소요시간 업데이트
                    heapq.heappush(Q, (alt, v, cnt - 1)) # 경유지 +1
        return -1        
