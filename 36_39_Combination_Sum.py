class Solution(object):      
    def combinationSum(self, candidates, target):
        
        def dfs(csum, index, path):
            """
            csum: 초기값을 target으로 초기화한 후 path 갱신될 때마다 차감
            index: 부모노드(자기자신)부터 시작할 수 있도록 넘겨주는 인덱스
            path: 현재까지의 조합
            """
            
            # 탐색 종료 조건
            if csum < 0: # path의 합이 target값을 초과한 경우
                return
            if csum == 0: # path의 합이 target값과 일치하는 경우
                result.append(path)
                return
            
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])
                
        
        result = []
        dfs(target, 0, [])
        
        return result
