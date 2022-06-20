class Solution(object):      
    def subsets(self, nums):
        
        def dfs(index, path):
            # 현재까지 path를 결과에 추가
            result.append(path)
            
            for i in range(index, len(nums)):
                # 자기자신 다음번 인덱스부터 시작
                dfs(i + 1, path + [nums[i]])
        
        
        result = []
        dfs(0, [])
        
        return result
