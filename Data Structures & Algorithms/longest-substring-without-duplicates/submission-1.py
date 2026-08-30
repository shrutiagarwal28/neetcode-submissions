class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uni_set = set()
        l, r = 0, 0
        maxLen = 0

        while l <= r and r < len(s):
            # uni_set.add(s[r])
            # r += 1
            # if s[l] == s[r]:
            #     while s[l] in uni_set and l <= r:
            #     uni_set.remove(s[l])
            #     l += 1

            
            while s[r] in uni_set and l <= r:
                uni_set.remove(s[l])
                l += 1
            uni_set.add(s[r])
            r += 1
            length = r-l
            maxLen = max(maxLen, length)
        
        return maxLen
