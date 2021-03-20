from bisect import bisect,bisect_left
class Solution:
	def rectangleArea(self,rectangles):
		Xs,Ys=set(),set()
		for i in rectangles:
			for j,k in enumerate(i):
				Ys.add(k) if j&1 else Xs.add(k)
		Xs,Ys=sorted(Xs),sorted(Ys)
		XsDict,YsDict=[{k:j for j,k in enumerate(i)} for i in (Xs,Ys)]
		rec=[[] for _ in range(len(Xs)-1)]
		for i in rectangles:
			le,ri=XsDict[i[0]],XsDict[i[2]] #以下部分本质上就是leetcode_57
			down,up=YsDict[i[1]],YsDict[i[3]]
			for j in range(le,ri):
				insert_down,insert_up=bisect(rec[j],down),bisect_left(rec[j],up)
				rec[j]=rec[j][:insert_down]+([down] if not insert_down&1 else [])+([up] if not insert_up&1 else [])+rec[j][insert_up:]
		return sum(sum((Ys[j[k+1]]-Ys[j[k]]) for k in range(0,len(j),2))*(Xs[i+1]-Xs[i]) for i,j in enumerate(rec))%int(1e9+7)