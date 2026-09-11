# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root_idx = 0
        inorder_idx_map = {val:idx for idx, val in enumerate(inorder)}

        def dfs(left, right):
            nonlocal root_idx
            if left > right: return None

            root_val = preorder[root_idx]
            root = TreeNode(root_val)
            root_idx += 1
            root.left = dfs(left, inorder_idx_map[root_val]-1)
            root.right = dfs(inorder_idx_map[root_val]+1, right)
            return root

        
        return dfs(0, len(inorder)-1)
