class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            prevEnd = res[-1][1]

            start, end = intervals[i][0], intervals[i][1]

            if prevEnd < start:
                res.append(intervals[i])

            elif prevEnd >= start:
                res[-1][1] = max(res[-1][1], end)
            
        return res

