class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, sum, path):
            # print(i, sum, path)
            if i >= len(nums) or sum > target:
                return
            if sum == target:
                # print("enter")
                res.append(path.copy())
                return

            
            path.append(nums[i])
            dfs(i, sum+nums[i], path)
            path.pop()
            dfs(i+1, sum, path)

        dfs(0, 0, [])

        return res