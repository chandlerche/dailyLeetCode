from collections import defaultdict
class Solution:
	def isRectangleCover(self,rectangles):
		xs=set()
		starts,ends=defaultdict(list),defaultdict(list)
		for i,j,p,q in rectangles:
			starts[i].append((j,q))
			ends[p].append((j,q))
			xs.add(i) or xs.add(p)
		xs=sorted(xs)
		first=sorted(starts[xs[0]]) #左边界
		prev=first[0][0]
		for i,j in first:
			if i!=prev:
				return False
			prev=j
		firstCol=[first[0][0],first[-1][-1]]
		last=sorted(ends[xs[-1]]) #右边界
		prev=last[0][0]
		for i,j in first:
			if i!=prev:
				return False
			prev=j
		lastCol=[last[0][0],last[-1][-1]]
		if firstCol!=lastCol:
			return False
		for i in xs[1:-1]:
			tmp=sorted(ends[i]) #end
			if not tmp:
				return False
			endCol=[]
			mark,prev=tmp[0]
			for p,q in tmp[1:]:
				if p!=prev:
					endCol.append((mark,prev))
					mark=p
				prev=q
			endCol.append((mark,prev))
			tmp=sorted(starts[i]) #start
			if not tmp:
				return False
			startCol=[]
			mark,prev=tmp[0]
			for p,q in tmp[1:]:
				if p!=prev:
					startCol.append((mark,prev))
					mark=p
				prev=q
			startCol.append((mark,prev))
			if startCol!=endCol: #如果start和end的范围不一样肯定错
				return False
		return True