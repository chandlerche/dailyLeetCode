class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        q = [(b,a,index) for index,(a,b) in enumerate(queries)]
        q.sort()
        #print(q)
        dit = collections.defaultdict(dict)
        self.idx = 0
        def insert(s):
            p = 0
            for i in range(30,-1,-1):
                u = (s>>i)&1
                dit[p].setdefault(u,{})
                if not dit[p][u]:
                    self.idx += 1
                    dit[p][u] = self.idx
                p = dit[p][u]
        def query(s):
            res,p = 0,0
            for i in range(30,-1,-1):
                u = s>>i&1
                if p not in dit:
                    return -1
                dit[p].setdefault(u,{})
                dit[p].setdefault(1-u,{})
                if dit[p][1-u]:
                    res |= 1<<i
                    p = dit[p][1-u]
                else:
                    p = dit[p][u]
            return res
        pos = 0
        n = len(nums)
        res = [-1]*len(q)
        for qq in q:
            while pos<n and nums[pos]<=qq[0]:
                insert(nums[pos])
                pos+=1
            res[qq[2]] = query(qq[1])
        return res