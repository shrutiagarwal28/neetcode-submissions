class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        # print(nums)

        def twoSum(idx, target):
            diff_dict = collections.defaultdict(int)
            for i in range(idx, len(nums)):
                if nums[i] in diff_dict:
                    return (i, diff_dict[i])
                diff = target - nums[i]
                diff_dict[i] = i
            
            # pass

        i = 0

        while i < len(nums):
            # print(i,res)
            if i != 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            
            if nums[i] > 0 : break

            x = i+1
            y = len(nums)-1

            while x < y:
                if nums[i] + nums[x] + nums[y] == 0:
                    res.append([nums[i], nums[x], nums[y]])
                    x += 1
                    y -= 1
                    while nums[x] == nums[x-1] and x < y:
                        x += 1
                elif nums[i] + nums[x] + nums[y] < 0:
                    x += 1
                else:
                    y -= 1

            i += 1
     
        return res