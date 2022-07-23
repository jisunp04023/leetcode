# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    longest = 0 # 가장 긴 경로
    def diameterOfBinaryTree(self, root):
        
        def dfs(node):
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 거리 = 왼쪽 상태값 + 오른쪽 상태값 + 2
            self.longest = max(self.longest, left + right + 2)
            
            # 상태값 = max(왼쪽 상태값, 오른쪽 상태값) + 1
            return max(left, right) + 1
        
        dfs(root)
        return self.longest
