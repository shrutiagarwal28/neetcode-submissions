class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        keep = 1
        prevEnd = intervals[0][-1]

        for start, end in intervals[1:]:
            if start < prevEnd:
                prevEnd = min(prevEnd, end)
            
            else:
                prevEnd = end
                keep += 1
        
        # print(keep)
        return len(intervals)-keep

