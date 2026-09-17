class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr_sum = n

        for i in range(n):
            xorr_sum = xorr_sum ^ i ^ nums[i]
        return xorr_sum