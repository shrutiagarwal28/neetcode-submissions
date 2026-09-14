"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adj_list = {}

        def dfs(node):
            if node in adj_list:
                return adj_list[node]

            if not node:
                return None
            
            node_copy = Node(node.val)
            adj_list[node] = node_copy

            for nei in node.neighbors:
                node_copy.neighbors.append(dfs(nei))

            return node_copy

        return dfs(node)