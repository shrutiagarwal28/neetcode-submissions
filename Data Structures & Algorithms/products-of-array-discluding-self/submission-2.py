class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         rhp = [1] * len(nums)
#         lhp = [1] * len(nums)
#         output = [1] * len(nums)

#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 rhp[i] = rhp[i] * nums[j]
        
#         for i in range(len(nums)-1, -1, -1):
#             for j in range(i-1, -1, -1):
#                 lhp[i] = lhp[i] * nums[j]

#         print(rhp, lhp)
#         for i in range(len(nums)):
#             output[i] = rhp[i]*lhp[i]
        
#         print(output)
#         return output
