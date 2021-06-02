import math
class Solution(object):
    def minSpeedOnTime(self, dist, hour):

        left = 1
        right = 10 ** 7 + 1
        ans = -1
        n = len(dist)

        def get_cost(speed):
            costs = 0
            for i in range(n):
                cost = dist[i] / speed
                costs += cost if i == n - 1 else math.ceil(cost)
            return costs

        while left < right:
            mid = (left + right) // 2
            if get_cost(mid) <= hour:
                ans = mid
                right = mid
            else:
                left = mid + 1

        return ans