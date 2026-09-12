class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            print("idx: ", l, mid, r)
            print("nums: ", nums[l], nums[mid], nums[r])
            if nums[l] <= nums[mid]:
                if nums[l] <=target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1 
            
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            

            # if target < nums[mid]: 
            #     if nums[l] < nums[mid] and nums[l] > nums[r] and target > nums[l]:
            #         r = mid - 1
            #     else:
            #         l = mid + 1
            # else:
            #     l = mid + 1
        return -1
                

