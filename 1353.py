from heapq import heappop,heappush
class Solution:
	def maxEvents(self,events):
		events.sort()
		heap=[]
		ans=eveIdx=0
		day=events[0][0]
		size=len(events)
		while heap or eveIdx<size:
			while eveIdx<size and events[eveIdx][0]==day:
				heappush(heap,events[eveIdx][1])
				eveIdx+=1
			while heap:
				if heappop(heap)>=day:
					ans+=1
					break
			day+=1
		return ans