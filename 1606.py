from sortedcontainers import SortedList
from heapq import heappop,heappush
class Solution:
	def busiestServers(self,k,arrival,load):
		cnt=[0]*k
		free=SortedList(range(k))
		busy=[]
		for ind,(start,interval) in enumerate(zip(arrival,load)):
			while busy:
				end,ind_=heappop(busy)
				if end>start:
					heappush(busy,(end,ind_))
					break
				else:
					free.add(ind_)
			if free:
				ind%=k
				pos=free.bisect_left(ind)
				if pos==len(free):
					pos=0
				heappush(busy,(start+interval,free[pos]))
				cnt[free.pop(pos)]+=1
		maxn=max(cnt)
		return [i for i,j in enumerate(cnt) if j==maxn]