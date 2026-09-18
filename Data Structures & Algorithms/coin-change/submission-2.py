class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        LIS = [float('inf') for a in range(amount+1)]
        coins.sort()
        LIS[0] = 0

        for i in range(1, amount+1):
            cur_sum = 0
            for coin in coins:
                if i - coin >= 0:
                    # print("enter", i, coin, LIS[i])
                    LIS[i] = min(LIS[i], LIS[i-coin]+1)

        print(LIS)
        return LIS[amount] if LIS[amount] != float('inf') else -1