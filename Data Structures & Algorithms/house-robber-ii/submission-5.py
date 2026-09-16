class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        one_back = 0
        two_back = 0

        for num in nums:
            new_rob = max(two_back+num, one_back)
            two_back = one_back
            one_back = new_rob
        
        return one_back