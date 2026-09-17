class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # idx = 0
        nums.sort()
        for i in range(n):
            # print(i, nums[idx], i^nums[idx])
            if nums[i]!= i:
                return i
            # idx += 1
        return n