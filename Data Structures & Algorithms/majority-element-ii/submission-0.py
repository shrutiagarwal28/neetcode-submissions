class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count_dict = Counter(nums)
        res = []

        for i, val in count_dict.items():
            if val > n//3:
                res.append(i)
        
        return res