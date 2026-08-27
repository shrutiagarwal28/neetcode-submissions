class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # for a palindrome we need that all letters appear 2 for even, and in odd, at most one char appears once
        freq_map = Counter(s)
        odds = sum(val % 2 for val in freq_map.values())
            
        return odds <= 1