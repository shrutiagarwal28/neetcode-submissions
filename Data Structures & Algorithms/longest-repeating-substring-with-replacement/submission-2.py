class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l, r = 0, 0
        freq_map = collections.defaultdict(int)

        while l <= r and r < len(s):
            freq_map[s[r]] += 1
            # print("window length: ",window_len, "l:", l, "r:", r, freq_map)
            while l<=r and not (r-l+1) - max(freq_map.values()) <= k:
                freq_map[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
            r += 1

        return longest
            

