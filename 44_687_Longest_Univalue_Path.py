# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    longest = 0 # 가장 긴 경로
    def longestUnivaluePath(self, root):
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 현재노드와 자식노드가 일치할 경우
            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0
                
            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0
            
            # 왼, 오 자식노드 간 거리의 합의 최댓값이 결과
            self.longest = max(self.longest, left + right)
            
            # 왼, 오 중 큰 값 리턴
            return max(left, right)
        
        dfs(root)
        return self.longest
