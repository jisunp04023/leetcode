from collections import defaultdict
import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        # 1. 모든 노드가 신호를 받을 수 있는가?
        # 2. 모든 노드에 도달할 때까지의 시간은?
        # = 가장 오래 걸리는 노드까지의 최단거리 => 다익스트라 알고리즘 이용
        
        # 그래프 저장
        graph = defaultdict(list)
        for _from, _to, time in times:
            graph[_from].append((_to, time))
            
        # 노드에 도착한 시간을 저장할 dictionary
        arrived = defaultdict(int)
        
        # [(소요시간, 시작노드)]
        # 소요시간을 기준으로 heapq에서 데이터를 뽑아냄
        queue = [(0, k)]
        
        while queue:
            time, node = heapq.heappop(queue)
            if node not in arrived:
                arrived[node] = time
                
                # 다음으로 이동할 수 있는 노드 탐색
                for _next, delay in graph[node]:
                    arrive_time = time + delay
                    heapq.heappush(queue, (arrive_time, _next))
        
        # 1. 모든 노드가 신호를 받았는가?
        if len(arrived) == n:
            # 2. 가장 오래 걸린 노드의 도달값은?
            return max(arrived.values())
        return -1
