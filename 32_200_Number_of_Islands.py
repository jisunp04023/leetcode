class Solution(object):  
    def numIslands(self, grid):
        
        # 현재 육지(1)와 '연결된' 육지를 전부 돌고 마킹함
        def dfs(i, j):
        
            # 육지(1)가 아닌 경우 종료
            if i < 0 or i >= row or \
                j < 0 or j >= col or \
                grid[i][j] != '1':
                    return
        
            # 방문한 육지(1)를 0으로 마킹해둠 (다시 방문하지 않도록)
            grid[i][j] = '0'
        
            # 동서남북 연결된 육지를 탐색
            dfs(i, j+1) # 동
            dfs(i, j-1) # 서
            dfs(i-1, j) # 남
            dfs(i+1, j) # 북
        
        
        
        row = len(grid)    # 행
        col = len(grid[0]) # 열
        
        count = 0 # 육지 개수
        
        # 행열 돌면서 육지(1)을 찾음
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1 # 현재 육지(1)와 '연결된' 육지를 다 돌았으니 육지 개수 +1
        
        return count
        
