import collections
class Solution:
    def balancedString(self, s: str) -> int:
        target = len(s)//4
        need ={'Q':target,'W':target,'E':target,'R':target}
        huan = collections.defaultdict(str)
        counter = collections.Counter(s)
        for cha in need:
            #要被替换的个数 注意是count=target!
            huan[cha]=counter[cha]-target
        left,right=0,0
        if self.match(huan):
            return 0
        res =len(s)+1
        while right<len(s):
            if s[right] in need:
                huan[s[right]]-=1
            while self.match(huan):
                res = min(res,right-left+1)
                if s[left] in counter:
                    huan[s[left]]+=1
                left+=1
            right+=1    
        return res

    def match(self,huan):
        for i in huan:
            if huan[i]>0:
                return False
        return True