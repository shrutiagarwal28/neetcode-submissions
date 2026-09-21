class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        len_dict = [False] * (len(s)+1)
        len_dict[n] = True

        for i in range(len(s)-1, -1, -1):
            len_dict[i] = any(s[i:i+len(word)] == word and len_dict[i+len(word)] for word in wordDict)

            # for word in wordDict:
            #     # print(i, word, s[i:i+len(word)])
            #     if(i+len(word)) <= n and s[i:i+len(word)] == word:
            #         len_dict[i] = len_dict[i+len(word)]
            #     if len_dict[i]:
            #         break
                    # remebeber to break out of the loop if you find the word otherwirse you will set dp[i] to wrong value by overwriting after true
        print(len_dict)
        
        return len_dict[0]