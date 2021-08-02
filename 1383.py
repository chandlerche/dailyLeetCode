import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD=10**9+7
        if k==1:
            return max([(efficiency[i]*speed[i])%MOD for i in range(n)])
        Person=[(efficiency[i],speed[i])for i in range(n)]
        #效率大的排前面,按照效率递减排序
        Person=sorted(Person)[::-1]
        mini_heap=[]
        res=0
        cur_sum=0
        for i in range(n):
            eff,spd=Person[i]
            #堆还没有满,新元素直接加入
            if i<k:
                heapq.heappush(mini_heap,spd)
                cur_sum+=spd
            #堆已经满了
            else:
                #堆顶(最小的速度)小于当前person的速度
                if mini_heap[0]<spd:
                    cur_sum=cur_sum-mini_heap[0]+spd
                    heapq.heappop(mini_heap)
                    heapq.heappush(mini_heap,spd)
            res=max(res,cur_sum*eff)
        return res%MOD