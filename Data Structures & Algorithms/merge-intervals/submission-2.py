class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        "Sort by start, then greedily merge each interval into the last one if they overlap — O(n log n) time, O(n) space."
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            prevEnd = res[-1][1]
            start, end = intervals[i][0], intervals[i][1]

            if prevEnd < start:
                res.append(intervals[i])

            else :
                res[-1][1] = max(res[-1][1], end)
            
        return res

