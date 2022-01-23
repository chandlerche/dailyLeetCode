import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 统一用num1和num2中更短的那个数组来操作
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2 , nums1)
        length = len(nums1) + len(nums2)
        cut1 , cut2 , cutL , cutR = 0 , 0 , 0 , len(nums1)
        while cut1 <= len(nums1):
            # cutL和cutR是真正走的指针，cut1和cut2是mid指针
            cut1 = cutL + (cutR - cutL) // 2
            cut2 = length // 2 - cut1
            # L1和R1是num1cut后左右两边的位置，L2和R2是num2的左右两点
            # 不需要切的时候，cut1和cut2会在0的位置，为了下面LR的大小比较，所以用极值来表示
            L1 = -math.inf if cut1 == 0 else nums1[cut1 - 1] #因为index从0开始，所以-1
            L2 = -math.inf if cut2 == 0 else nums2[cut2 - 1]
            R1 =  math.inf if cut1 == len(nums1) else nums1[cut1]
            R2 =  math.inf if cut2 == len(nums2) else nums2[cut2]
            if L1 > R2: # 说明应该左移，把右指针移到mid指针-1
                cutR = cut1 - 1
            elif L2 > R1: # 说明应该右移，把左指针移到mid指针+1
                cutL = cut1 + 1
            # 按奇偶情况处理
            else:
                if length % 2 == 0:
                    L1 = L1 if L1 > L2 else L2 #L1和L2取最大值
                    R1 = R1 if R1 < R2 else R2 #R1和R2取最小值
                    return float(L1 + R1) / 2
                else:
                    R1 = R1 if R1 < R2 else R2
                    return float(R1)
        return -1.0