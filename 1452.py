class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        res = []
        for i in range(len(favoriteCompanies)):
            # 待判断的集合
            d = set(favoriteCompanies[i])
            
            # 去掉待判断集合后的数组
            temp = favoriteCompanies[0:i]+favoriteCompanies[i+1:]
            
            # 标志位，判断是否需要将i添加到结果集中
            flag = True
            for j in range(len(temp)):
                c = set(temp[j])
                # 如果d是c的子集合，更新标志，跳出循环
                if d.issubset(c):
                    flag = False
                    break

            if flag:
                # 程序执行到这里，说明c是满足条件，将i添加到结果集就行  
                res.append(i)
        return res