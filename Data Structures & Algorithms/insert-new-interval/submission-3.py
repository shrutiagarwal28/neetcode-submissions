class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        n_start = newInterval[0]
        n_end = newInterval[1]
        # prevStart = intervals[0][0]
        # prevEnd = intervals[0][1]
        breaker = 0

        for i, (start, end) in enumerate(intervals):
            if end < n_start:
                res.append([start, end])

            elif start > n_end:
                res.append([n_start,n_end])
                return res + intervals[i:]

            elif start <= n_end:
                n_start = min(n_start, start)
                n_end = max(n_end, end)

            
        res.append([n_start,n_end])
        
        return res
        
        
        