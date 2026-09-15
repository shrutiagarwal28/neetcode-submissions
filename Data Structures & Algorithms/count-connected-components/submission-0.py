class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_map = collections.defaultdict(list)
        for x,y in edges:
            adj_map[x].append(y)
            adj_map[y].append(x)
        
        components = 0
        visited = set()

        def dfs(node):
            if node in visited: 
                return 
            
            visited.add(node)

            for nei in adj_map[node]:
                dfs(nei)
        
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)
        
        return components
            
            
