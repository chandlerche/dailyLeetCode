class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if len(intervals) <= 1:
            return True
        intervals.sort(key=lambda i: i.start)

        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False

        return True
