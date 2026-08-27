class Solution:
    def countElements(self, arr: List[int]) -> int:
        freq_map = Counter(arr)
        count = 0
        for num in arr:
            if num+1 in freq_map:
                count += 1
                freq_map[num] -= 1
        return count