class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:


        # 方法一：差分 + 哈希表 + 动态规划
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n^2)
        n = len(nums)
        if n < 3:
            return 0

        hash_table = [defaultdict(list) for _ in range(n)]
        #print('hash_table:', hash_table)
        #print(hash_table[0])
        #print('------')
        count = 0

        for i in range(1, n):
            for j in range(i-1, -1, -1):
                diff = nums[i] - nums[j]
                if hash_table[i][diff]:
                    hash_table[i][diff] += (hash_table[j][diff] or 0) + 1
                else:
                    hash_table[i][diff] = (hash_table[j][diff] or 0) + 1                    
                #print(i, j, diff, hash_table)
                if hash_table[j][diff] :
                    count += hash_table[j][diff] 

        return count