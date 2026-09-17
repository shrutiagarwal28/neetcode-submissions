from _heapq import heapify
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        intervals.sort(key = lambda x: x.start)

        for interval in intervals:
            s = interval.start
            e = interval.end

            if rooms and rooms[0] <= s:
                heapq.heappop(rooms)
            heapq.heappush(rooms, e)
        return len(rooms)