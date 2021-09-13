class UF:
	def __init__(self,n):
		self.p=[*range(n+1)]
	def find(self,i):
		if self.p[i]!=i:
			self.p[i]=self.find(self.p[i])
		return self.p[i]
	def union(self,i,j):
		p_i=self.find(i)
		p_j=self.find(j)
		if p_i!=p_j:
			self.p[p_j]=p_i
class Solution:
	def areConnected(self,n,threshold,queries):
		uf=UF(n)
		for i in range(n,threshold,-1):
			p=n-n%i
			for j in range(p,0,-i):
				uf.union(p,j)
		ans=[]
		for i,j in queries:
			ans.append(uf.find(i)==uf.find(j))
		return ans