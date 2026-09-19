class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minp = 1
        maxp = 1
        currp = max(nums)

        for num in nums:
            tmp = maxp
            maxp = max(maxp*num, minp*num,num)
            minp = min(minp*num, tmp*num, num)
            # print  (maxp, minp, tmp, currp)
            currp = max(minp, maxp, currp)
            
        return currp