# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        output = []

        def dfs(node):
            if not node:
                output.append("N")
                return 
            output.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(output)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        data1 = data.split(",")
        root_idx = 0

        def dfs():
            nonlocal root_idx
            root_val = (data1[root_idx])
            # print(root_val, root_idx)
            root_idx += 1
            if root_val  == 'N':
                return None
            root_val = int(root_val)
            root = TreeNode(root_val)

            
            root.left = dfs()
            root.right = dfs()

            return root
        head = dfs()
        return head



