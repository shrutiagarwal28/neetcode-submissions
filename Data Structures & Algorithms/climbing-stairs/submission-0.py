class Solution:
    def climbStairs(self, n: int) -> int:
    #    Top Down:
        cache = [-1]*n

        def dfs(node):
            if node >= n:
                return node == n

            if cache[node] != -1:
                return cache[node]

            cache[node] = dfs(node+1) + dfs(node+2)

            return cache[node]
        
        return dfs(0)