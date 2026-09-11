# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            nonlocal max_sum
            left_path = max(dfs(node.left),0)
            right_path = max(dfs(node.right),0)
            total_sum = left_path + node.val + right_path
            # print(node.val, left_path, right_path, total_sum)
            max_sum = max(max_sum, total_sum)
            return max( node.val + right_path, node.val + left_path)
 
        dfs(root)
        return max_sum

