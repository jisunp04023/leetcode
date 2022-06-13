class Solution(object):  
    def letterCombinations(self, digits):
        
        def dfs(index, path):
            # digits 자리수만큼 탐색했다면 종료
            if len(path) == len(digits):
                result.append(path)
                return
            
            # digits 자리수만큼 돌면서 재귀 dfs 탐색
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)
        
        
        if not digits:
            return []
        
        dic = {'2' : 'abc',
               '3' : 'def',
               '4' : 'ghi',
               '5' : 'jkl',
               '6' : 'mno',
               '7' : 'pqrs',
               '8' : 'tuv',
               '9' : 'wxyz'}
        
        result = []
        
        dfs(0, "")
        
        return result
