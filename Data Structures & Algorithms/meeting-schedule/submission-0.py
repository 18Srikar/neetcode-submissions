"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        arr=[]
        for each in intervals:
            arr.append((each.start,each.end))
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i][1]>arr[i+1][0]:
                return False
        return True
