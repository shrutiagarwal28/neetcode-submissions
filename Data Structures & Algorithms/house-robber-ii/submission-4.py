class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robbery(houses):
            if len(houses) <= 2:
                return max(houses)
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(dp[0], houses[1])

            for i in range(2, len(houses)):
                dp[i] = max(dp[i-2]+houses[i], dp[i-1])
            print(dp)
            return dp[-1]

        max_robbed = max(robbery(nums[1:]), robbery(nums[:-1]))

        return max_robbed