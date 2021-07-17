class Solution:
    def findSubsequences(self, nums: list) -> list:

        all_list = {}
        
        for i in nums:
            # 把单个数字也当做一个递增子序列，以便后续计算
            new_list = [[i]]
            # 遍历字典中所有结尾数字key小于等于当前数字的情况，将其所有递增子序列加上当前数字
            for j in all_list:
                if j <= i:
                    for k in all_list[j]:
                        new_list.append(k + [i])
            # 此时的new_list，就是遍历到i时，以数字i结尾的所有递增子序列
            all_list[i] = new_list

        result = []
        for i in all_list:
            # 从下标1开始的原因是，去掉由单个数字组成的递增子序列
            for j in range(1, len(all_list[i])):
                result.append(all_list[i][j])

        return result