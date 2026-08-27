class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # create a dictionary to map where nums2's ind occur
        # when traversing nums1, put in the value that you look up in O(1) time from the first dictionary

        nums2_map = {val:i for i, val in enumerate(nums2)}
        res = []
        print(nums2_map)
        for j, num in enumerate(nums1):
            res.append(nums2_map[num])
        return res
