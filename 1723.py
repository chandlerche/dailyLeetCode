class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def check(limit):
            w=[0]*k     # 存放每个工人当前的工作时间
            def dfs(index):
                if index==n: return True
                cur=jobs[index]
                for i in range(k):
                    if w[i]+cur<=limit:
                        w[i]+=cur
                        if dfs(index+1):
                            return True
                        w[i]-=cur
                    if w[i]==0: # 如果当前工人未被分配工作，那么下一个工人也必然未被分配工作
                        break
                return False
            return dfs(0)
        jobs.sort(reverse=True)
        n=len(jobs)
        l,r=jobs[0],sum(jobs)
        while l<r:
            mid=(l+r)//2
            if check(mid):
                r=mid
            else:
                l=mid+1
        return l