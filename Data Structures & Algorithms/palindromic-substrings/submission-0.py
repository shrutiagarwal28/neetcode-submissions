class Solution:
    def countSubstrings(self, s: str) -> int:
        # max_len = 0
        result = []

        def is_pal(l,r):
            # nonlocal max_len, result
            # length = 0
            while 0 <= l and r < len(s):
                if s[l] == s[r]:
                    result.append(s[l:r+1])
                    
                    l -= 1
                    r += 1
                else:
                    break

        for i in range(len(s)):
            is_pal(i,i)
            is_pal(i-1,i)

        return len(result) 