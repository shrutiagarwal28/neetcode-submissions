class Solution:
    def climbStairs(self, n: int) -> int:
    #    Top Down:
        # cache = [-1]*n

        # def dfs(node):
        #     if node >= n:
        #         return node == n

        #     if cache[node] != -1:
        #         return cache[node]

        #     cache[node] = dfs(node+1) + dfs(node+2)

        #     return cache[node]
        
        # return dfs(0)

    #    Bottom Up:
        # if n <= 2:
        #     return n
        # dp = [0]*(n+1)
        # dp[1], dp[2] = 1, 2

        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        
        # return dp[n]

        one = 1
        two = 1

        for i in range(n-1):
            tmp = one
            one = two + one
            two = tmp
        
        return one

        