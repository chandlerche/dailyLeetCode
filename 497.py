import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.area = [0]*(len(rects)+1)
        for i in range(1,len(rects)+1):
            rect = rects[i-1]
            area = (rect[2]-rect[0]+1)*(rect[3]-rect[1]+1)
            self.area[i] = self.area[i-1]+area
        

    def pick(self) -> List[int]:
        d = random.randint(1,self.area[-1])
        # 二分
        l,r = 1,len(self.rects)
        index = 0
        while l<=r:
            m = (l+r)//2
            if d<=self.area[m] and d>self.area[m-1]:
                index = m-1
                break
            if d>self.area[m]:
                l = m + 1
            else:
                r = m - 1
        xl,xr = self.rects[index][0],self.rects[index][2]
        yl,yr = self.rects[index][1],self.rects[index][3]
        x = random.randint(xl,xr)
        y = random.randint(yl,yr)
        return [x,y]