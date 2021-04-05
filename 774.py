class Solution(object):
    def minmaxGasDist(self, st, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        lf = 1e-6
        rt = st[-1] - st[0]
        eps = 1e-7
        while rt - lf > eps:
            mid = (rt + lf) / 2
            cnt = 0
            for a, b in zip(st, st[1:]):
               cnt += (int)((b - a) / mid)
            if cnt <= K: rt = mid
            else: lf = mid
        return rt