class Solution:
    from heapq import nsmallest

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return nsmallest(K,points,key=lambda x:x[0]**2+x[1]**2)