class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        len_dict = [False] * (len(s)+1)
        len_dict[n] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                # print(i, word, s[i:i+len(word)])
                if(i+len(word)) <= n and s[i:i+len(word)] == word:
                    len_dict[i] = len_dict[i+len(word)]
                if len_dict[i]:
                    break
        print(len_dict)
        
        return len_dict[0]