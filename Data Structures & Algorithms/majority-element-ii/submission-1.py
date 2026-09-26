class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        l, r = 0, 0
        res = []

        while r < len(nums) and l <= r:
            
            while r < len(nums) and nums[l] == nums[r]:   
                r += 1
            if (len(nums)//3) < (r-l):
                res.append(nums[l]) 
                
            l = r
            
        return res
            

