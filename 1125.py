class Solution:
	def smallestSufficientTeam(self,req_skills,people):
		legt=len(req_skills)
		end,table=legt-1,dict(zip(req_skills,range(16)))
		bins,dp=[],[[] for _ in range(2<<end)]
		for i,skills in enumerate(people):
			if skills:
				tmp=["0"]*legt
				for skill in skills:
					tmp[end-table[skill]]="1"
				bins.append((int("".join(tmp),base=2),i))
		for num,person in bins:
			new_dp=dp[:]
			for idx,comb in enumerate(dp):
				if not idx or comb:
					tmp=idx|num
					new_comb=new_dp[idx]+[person]
					new_dp[tmp]=new_comb if not new_dp[tmp] or len(new_comb)<len(new_dp[tmp]) else new_dp[tmp]
			dp=new_dp
		return dp[-1]