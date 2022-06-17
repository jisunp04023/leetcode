class Solution(object):      
    def permute(self, nums):
        
        def dfs(elements):
            # element 다 뽑았다면 결과에 추가
            if not len(elements):
                result.append(PREV[:])
                return
            
            for i in elements:
                # 다음 dfs의 input을 NEXT에 저장
                NEXT = elements[:]
                NEXT.remove(i)
                
                # 지금까지의 path를 PREV에 저장
                PREV.append(i)
                dfs(NEXT)
                PREV.pop()
        
        
        result = []
        PREV = []
        dfs(nums)
        
        return result
