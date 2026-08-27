class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # for a palindrome we need that all letters appear 2 for even, and in odd, at most one char appears once
        freq_map = Counter(s)
        if not len(s)%2:
            for char, count in freq_map.items():
                if count%2 :
                    return False
        else:
            mid_val =False
            for char, count in freq_map.items():
                if mid_val and count%2:
                    # print(odd)
                    return False
                elif not mid_val and count == 1:
                    mid_val = True
            
        return True