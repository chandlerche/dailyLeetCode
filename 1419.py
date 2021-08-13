class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        dic = {'c':0, 'r':0, 'o':0, 'a':0, 'k':0}
        for i in croakOfFrogs:
            dic[i] += 1
        if not dic['c'] == dic['r'] == dic['o'] == dic['a'] == dic['k']:
            return -1
        
        m = 0
        dic = {'c':0, 'r':0, 'o':0, 'a':0, 'k':0}
        for i in range(len(croakOfFrogs)):
            dic[croakOfFrogs[i]] += 1
            if not (dic['c'] >= dic['r'] >= dic['o'] >= dic['a'] >= dic['k']):
                return -1
            if all(val > 0 for val in list(dic.values())):
                for c in 'croak':
                    dic[c] -= 1
            else:
                m = max(m, dic['c'])
        return m