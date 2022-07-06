from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        traced = set() # 중복 노드를 검사하여 사이클을 검사
        visited = set() # 이미 방문한 즉, 이미 검증된 노드
        # visited로 가지치기가 가능해져 속도 향상

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)

            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)

            visited.add(i)
            return True

        for x in list(graph):
            print(x)
            if not dfs(x):
                return False

        return True
