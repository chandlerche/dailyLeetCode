class Solution:
	def oddEvenJumps(self,A):
		size=len(A)

		sort1=sorted(enumerate(A),key=lambda x:(x[1],x[0]))
		oddJumpNxt=[-1]*size
		stack=[]
		for i,_ in sort1:
			while stack and stack[-1]<i:
				oddJumpNxt[stack.pop()]=i
			stack.append(i)

		sort2=sorted(enumerate(A),key=lambda x:(-x[1],x[0]))
		evenJumpNxt=[-1]*size
		stack=[]
		for i,_ in sort2:
			while stack and stack[-1]<i:
				evenJumpNxt[stack.pop()]=i
			stack.append(i)

		ret=1
		ans=[[False]*2 for _ in range(size)];ans[-1]=[True]*2
		for i in range(size-2,-1,-1):
			if oddJumpNxt[i]!=-1 and ans[oddJumpNxt[i]][1]:
				ans[i][0]=True
				ret+=1
			if evenJumpNxt[i]!=-1 and ans[evenJumpNxt[i]][0]:
				ans[i][1]=True
		return ret