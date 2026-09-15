class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False
        
        adj_map = collections.defaultdict(list)
        for x,y in edges:
            adj_map[x].append(y)
            adj_map[y].append(x)
        
        visited = set()

        def dfs(curr, par):
            if curr in visited:
                return False
            
            visited.add(curr)

            for nei in adj_map[curr]:
                if nei == par:
                    continue
                if not dfs(nei, curr):
                    return False
            
            return True
        check = dfs(0,None)

        return check and len(visited) == n

        # for node in range(n):
        #     if not dfs(node, None):
        #         return False
        
        # return True

        