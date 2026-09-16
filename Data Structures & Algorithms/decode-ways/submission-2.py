class Solution:
    def numDecodings(self, s: str) -> int:
        # al = "abcdefghijklmnopqrstuvxwyz"
        # # num_alpha_map = {i+1:alph for i, alph in enumerate(al)}
        # num_map = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'x', 24: 'w', 25: 'y', 26: 'z'}

        if s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n+1)
        dp[len(s)] = 1

        for i in range(len(s)-1, -1, -1):
            print(i, s[i], s[i:i+2])
            if int(s[i]) == 0:
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
                if i < n-1 and 0 < int(s[i]) and 9 < int(s[i:i+2]) <= 26:
                # print("enter")
                    dp[i] += dp[i+2] 
                # print(dp)
            
        
        return dp[0]


