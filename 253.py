class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        startTimes = [i[0] for i in intervals]
        endTimes = [i[1] for i in intervals]
        startTimes = sorted(startTimes)
        endTimes = sorted(endTimes)
        rooms = 0
        while(len(startTimes) > 0):
            startTime = startTimes.pop(0)
            #now a meeting is going to start, is there a meeting ends
            #(meaning a meeting room is released)?
            endTime = endTimes[0]
            if endTime <= startTime:
                endTimes.pop(0)
            else:
                #need to ask for a new room
                rooms += 1
        return rooms