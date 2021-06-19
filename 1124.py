class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        for i in range(len(hours)):hours[i] = 1 if hours[i]>8 else -1
        ans ,d = max(0,hours[0]),{hours[0]:0}
        for i in range(1,len(hours)):
            hours[i] += hours[i-1]
            ans = max(ans,i-d.get(hours[i]-1,i),i+1 if hours[i]>0 else 0)
            if hours[i] not in d:d[hours[i]]=i
        return ans