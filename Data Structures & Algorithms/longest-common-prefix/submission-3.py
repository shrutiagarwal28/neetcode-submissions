class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = "" 
        idx = 0

        while True:
            if idx < len(strs[0]):
                prefix += strs[0][idx] 
            else: return prefix
            for word in strs[1:]:
                if idx == len(word) or (prefix and word[idx] != prefix[-1]):
                    
                    return prefix[:-1]
            
            idx += 1
        
        return prefix
        
