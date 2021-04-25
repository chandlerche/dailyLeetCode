class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        m=max(instructions)
        fenwicktree=[0]*(m+1)
        def query(i):
            res=0
            while i>0:
                res+=fenwicktree[i]
                i-=i&(-i)
            return res
        def update(i,delta):
            while i<=m:
                fenwicktree[i]+=delta
                i+=i&(-i)
        ans=0
        for num in instructions:
            ans+=min(query(num-1),query(m)-query(num))
            update(num,1)
        return ans%(10**9+7)