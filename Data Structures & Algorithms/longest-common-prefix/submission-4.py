class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = "" 
        idx = 0

        while idx < len(strs[0]):
            # if idx < len(strs[0]):
            #     prefix += strs[0][idx] 
            # else: 
            #     return prefix
            prefix += strs[0][idx]
            for word in strs[1:]:
                if idx == len(word) or  word[idx] != prefix[-1]:
                    
                    return prefix[:-1]
            
            idx += 1
        
        return prefix
        
