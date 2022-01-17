class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        from collections import defaultdict
        A=defaultdict(list)
        for i,j in edges:
            A[i].append(j)
            A[j].append(i)
        visited=set()
        def helper(node,k):
            visited.add(node)
            m=sum(i not in visited for i in A[node])          
            return node==target if k*m==0 else sum(helper(i,k-1) for i in A[node] if i not in visited)/m
        return helper(1,t) 