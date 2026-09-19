class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n+1)
        dp[n-1] = True

        for i in range(n-1, -1, -1):
            for j in range(nums[i]+1):
                print(i, j)
                if dp[i+j]:
                    dp[i] = True
                    break
        print(dp)
        return dp[0]