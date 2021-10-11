class Solution(Object):

    def numWays(self , n , k):
        if n == 0: return 0
        if n == 1: return k

        same = 0
        diff = k
        total = k
        for i in range(2 , n + 1):
            same = diff # 我们当前涂相同颜色，代表我们之前涂的是不同颜色
            diff = (k - 1) * total #当前涂不同，则当前能涂的种类是(k - 1) * 之前能涂的种类
            total = same + diff # 一共能涂的是相同的加不同的
        return total