class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        hashmap = collections.defaultdict(list)  #创建一个值是列表的字典
        xMin,xMax = 10**5,-10**5  #初始化最小值和最大值

        for i,vec in enumerate(nums):  #把每个数字出现过的列表添加到字典该数作为键，值的列表中
            for x in vec:
                hashmap[x].append(i)  #添加对应值
            xMin = min(xMin,*vec)
            xMax = max(xMax,*vec)  #找到数字所在范围 

        freq = [0] * n  #在当前窗口的情况下对应列表编号的出现次数
        inside = 0  #窗口中已有的列表数
        left,right = xMin,xMin-1  #两个指针的初始位置
        bestLeft,bestRight = xMin,xMax  #返回窗口的初始位置

        while right < xMax:  #指针对应的是整数值，在范围内每次加1遍历
            """
            指向窗口右边界的指针右移当且仅当每次遍历到新的元素，并将这个新的元素对应的值数组中的每一个数加入到哈希表中
            """
            right += 1
            if right in hashmap:  #这个数出现在了之前的列表中
                for x in hashmap[right]:  #遍历这个数出现过的每一个列表编号
                    freq[x] += 1  #在当前窗口的情况下对应列表编号的出现次数+1
                    if freq[x] == 1:  #如果对应列表初次出现了 窗口中就出现了新列表 此时窗口中已有列表数+1
                        inside += 1 
            while inside == n:  #窗口中已经包含了全部的列表 
                """
                答案更新当且仅当当前窗口内的元素包含 A 中所有的元素
                """
                if right - left < bestRight - bestLeft:  #维护最小窗口
                    bestLeft,bestRight = left,right 
                if left in hashmap:
                    """
                    指向窗口右边界的指针右移当且仅当每次遍历到新的元素，并将这个新的元素对应的值数组中的每一个数加入到哈希表中
                    """
                    for x in hashmap[left]:
                        freq[x] -= 1 
                        if freq[x] == 0:  #对应列表出现次数为0 也就是不见了
                            inside -= 1  #窗口中对应列表数就-1
                left += 1  #左指针向右移动 也就是题解里说的 指向窗口左边界的指针右移当且仅当当前窗口内的元素包含 A 中所有的元素，同时将原来左边界对应的值数组的元素们从哈希表中移除

        return [bestLeft,bestRight]