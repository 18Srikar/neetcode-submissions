class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort in-place by start time: O(n log n) time, O(1) extra space
        intervals.sort(key=lambda i: i.start)
        
        # Check for overlaps
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
                
        return True
