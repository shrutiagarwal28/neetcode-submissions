class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        min_ele = nums[0]

        while l < r and r < n:
            mid = (r+l) // 2
            print(l, mid, r)

            # if nums[l] < nums[r]:
            #     min_ele = min(min_ele, nums[l])
            #     break
            
            # min_ele = min(min_ele, nums[mid])

            if nums[mid] < nums[r]:
                r = mid 
            else:
                l = mid + 1

                
        return nums[l]