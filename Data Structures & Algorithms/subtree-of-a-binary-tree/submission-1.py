# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subroot:
            return False

        def isSame(node1, node2):
            
            if not node1 and not node2:
                return True
            
            if node1 and node2 and node1.val == node2.val:
                return isSame(node1.left, node2.left) and isSame(node1.right, node2. right)
            return False

        stack = [root]
        # curr = root
        while stack:
            curr = stack.pop()
            if curr.val == subRoot.val:
                if isSame(curr, subRoot):
                    return True
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return False
            
