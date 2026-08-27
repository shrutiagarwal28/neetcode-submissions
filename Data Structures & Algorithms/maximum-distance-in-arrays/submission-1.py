class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        global_min = arrays[0][0]
        global_max = arrays[0][-1]
        res = 0

        for i in range(1, len(arrays)):
            array = arrays[i]
            res = max(res, abs(global_max - array[0]), abs(array[-1]-global_min))
            global_max = max(global_max, array[-1])
            gloabl_min = min(global_min, array[0])

        return res