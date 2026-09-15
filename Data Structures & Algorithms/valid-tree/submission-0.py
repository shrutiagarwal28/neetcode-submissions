class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
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

        if check and len(visited) == n: return True

        # for node in range(n):
        #     if not dfs(node, None):
        #         return False
        
        return False

        