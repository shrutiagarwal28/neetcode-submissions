class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_count = Counter(s)
        for t_char in t:
            s_char_count[t_char] -= 1
            if s_char_count[t_char] < 0:
                return False
        
        for count in s_char_count.values():
            if count != 0:
                return False

        return True