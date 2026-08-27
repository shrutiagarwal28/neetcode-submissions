class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        uni_set = set()
        dup_set = set()

        for num in nums:
            if num in uni_set:
                uni_set.remove(num)
                dup_set.add(num)
            elif num not in uni_set and num not in dup_set:
                uni_set.add(num)
        
        return max(uni_set) if uni_set else -1