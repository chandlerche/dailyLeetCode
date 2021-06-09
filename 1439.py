from heapq import heappop,heappush
class Solution:
	def kthSmallest(self,mat,k):
		row,col=len(mat),len(mat[0]) #行数 列数
		heap=[(sum(i[0] for i in mat),(0,)*row)] #包含两个元素的元组 前面一个是各个数字的和 后面一个是各行选中的数字的列数
		ans,n=0,1 #答案 当前要寻找第n个最小的数字和了
		visit=set() #可能会有重复访问 所以需要使用set来判断
		while n<=k:
			total,idxs=heappop(heap)
			if idxs not in visit:
				visit.add(idxs)
				for i in range(row): #对于每行都要进行拓展
					ttotal,tidxs=total,list(idxs)
					tidxs[i]+=1
					if tidxs[i]!=col:
						ttotal+=mat[i][tidxs[i]]-mat[i][tidxs[i]-1]
						heappush(heap,(ttotal,tuple(tidxs)))
				n+=1
				ans=total
		return ans