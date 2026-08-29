class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seq_set = set(nums)

        for i in range(len(nums)):
            num = nums[i]
            if num-1 not in seq_set:
                length = 1
                while num+length in seq_set:
                    length += 1
                longest = max(longest, length)
        
        return longest
                    